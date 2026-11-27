"""Refresh citation metrics from the public Google Scholar profile's first page."""

import json
import os
import re
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import parse_qs, urlencode, urljoin, urlsplit
from urllib.request import HTTPRedirectHandler, Request, build_opener

from lxml import etree
from lxml.html import fromstring


PROFILE = "https://scholar.google.com/citations"
RESULTS = Path("results")
STATS = RESULTS / "gs_data.json"
BADGE = RESULTS / "gs_data_shieldsio.json"
METRICS = ("citedby", "citedby5y", "hindex", "hindex5y", "i10index", "i10index5y")


class ScholarUnavailable(Exception):
    """The upstream response did not contain a usable profile."""


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def fetch_profile(scholar_id):
    # Google Scholar robots.txt allows /citations?user=... but excludes cstart
    # pagination and /scholar. Fetch this first profile page once, without rotating proxies.
    url = f"{PROFILE}?{urlencode({'user': scholar_id, 'hl': 'en', 'pagesize': 100})}"
    request = Request(url, headers={
        "User-Agent": "AcapageCitationUpdater/1.0 (+https://github.com/xyjigsaw/acapage)",
        "Accept": "text/html",
    })
    try:
        with build_opener(NoRedirect()).open(request, timeout=25) as response:
            body = response.read(2_000_001)
            if response.headers.get_content_type() != "text/html" or len(body) > 2_000_000:
                raise ScholarUnavailable("unexpected profile response type or size")
            return body
    except HTTPError as exc:
        raise ScholarUnavailable(f"profile request returned HTTP {exc.code}") from exc
    except (URLError, TimeoutError, OSError) as exc:
        raise ScholarUnavailable(f"profile request failed: {type(exc).__name__}") from exc


def number(value):
    value = value.strip().rstrip("*∗").strip().replace(",", "")
    if not re.fullmatch(r"[0-9]+", value):
        raise ScholarUnavailable("missing or unrecognized citation count")
    return int(value)


def class_nodes(node, css_class, tag="*"):
    return node.xpath(
        f".//{tag}[contains(concat(' ', normalize-space(@class), ' '), $token)]",
        token=f" {css_class} ",
    )


def node_text(node):
    return " ".join(node.text_content().split())


def parse_profile(html, scholar_id, previous):
    try:
        page = fromstring(html)
    except (etree.ParserError, ValueError) as exc:
        raise ScholarUnavailable("public profile HTML could not be parsed") from exc
    name = page.get_element_by_id("gsc_prf_in", None)
    metrics_table = page.get_element_by_id("gsc_rsb_st", None)
    publications_table = page.get_element_by_id("gsc_a_b", None)
    cells = class_nodes(metrics_table, "gsc_rsb_std", "td") if metrics_table is not None else []
    rows = class_nodes(publications_table, "gsc_a_tr", "tr") if publications_table is not None else []
    if name is None or not node_text(name) or len(cells) != 6 or not rows:
        raise ScholarUnavailable("profile table is missing or its markup changed")
    next_button = page.get_element_by_id("gsc_bpf_next", None)
    if next_button is not None and "disabled" not in next_button.attrib and next_button.get("aria-disabled") != "true":
        raise ScholarUnavailable("profile needs pagination; refused to publish a partial snapshot")

    previous_papers = previous["publications"]
    publications = {}
    for row in rows:
        titles = class_nodes(row, "gsc_a_at", "a")
        citation_cells = class_nodes(row, "gsc_a_c")
        if len(titles) != 1 or len(citation_cells) != 1 or not node_text(titles[0]) or not titles[0].get("href"):
            raise ScholarUnavailable("publication table is incomplete")
        title, citations = titles[0], citation_cells[0]
        paper_id = parse_qs(urlsplit(title.get("href")).query).get("citation_for_view", [""])[0]
        if not paper_id.startswith(f"{scholar_id}:") or paper_id in publications:
            raise ScholarUnavailable("profile identifier mismatch or duplicate publication")
        entry = dict(previous_papers.get(paper_id, {}))
        bib = dict(entry.get("bib", {}))
        bib["title"] = node_text(title)
        details = class_nodes(row, "gs_gray")
        if len(details) >= 2:
            bib["citation"] = node_text(details[1])
        years = class_nodes(row, "gsc_a_h")
        if years and node_text(years[0]):
            bib["pub_year"] = node_text(years[0])
        links = [a for a in class_nodes(citations, "gsc_a_ac", "a") if a.get("href")]
        link = links[0] if links else None
        count = node_text(link) if link is not None else node_text(citations)
        entry.update({
            "container_type": "Publication",
            "source": "AUTHOR_PUBLICATION_ENTRY",
            "filled": False,
            "bib": bib,
            "author_pub_id": paper_id,
            "num_citations": number(count) if count else 0,
        })
        if link is not None and count:
            full_url = urljoin(PROFILE, link.get("href"))
            parts = urlsplit(full_url)
            ids = parse_qs(parts.query).get("cites", [""])[0].split(",")
            if parts.scheme == "https" and parts.hostname == "scholar.google.com" and all(
                re.fullmatch(r"[0-9]+", item) for item in ids
            ):
                entry.update(citedby_url=full_url, cites_id=ids)
        elif not count:
            entry.pop("citedby_url", None)
            entry.pop("cites_id", None)
        publications[paper_id] = entry

    if previous_papers and (len(publications) < len(previous_papers)
                            or not publications.keys() & previous_papers.keys()):
        raise ScholarUnavailable("profile response may be truncated or belong to another author")

    stats = {**previous, **dict(zip(METRICS, [number(node_text(cell)) for cell in cells]))}
    stats.update(scholar_id=scholar_id, name=node_text(name), publications=publications)
    chart = page.get_element_by_id("gsc_g", None)
    years = [node_text(n) for n in class_nodes(chart, "gsc_g_t")] if chart is not None else []
    counts = [node_text(n) for n in class_nodes(chart, "gsc_g_al")] if chart is not None else []
    if years and len(years) == len(counts) and all(re.fullmatch(r"[0-9]{4}", y) for y in years):
        stats["cites_per_year"] = dict(zip(years, map(number, counts)))
    stats["updated"] = datetime.now(timezone.utc).replace(tzinfo=None).isoformat(sep=" ")
    return stats


def main():
    scholar_id = os.environ["GOOGLE_SCHOLAR_ID"]
    if not re.fullmatch(r"[A-Za-z0-9_-]{8,32}", scholar_id):
        raise ValueError("invalid Google Scholar profile identifier")
    previous = json.loads(STATS.read_text(encoding="utf-8"))
    if previous.get("scholar_id") != scholar_id:
        raise ValueError("configured Google Scholar profile does not match the published snapshot")
    try:
        stats = parse_profile(fetch_profile(scholar_id), scholar_id, previous)
    except ScholarUnavailable as exc:
        if BADGE.is_file():
            print(f"Google Scholar not refreshed; retaining previous data: {exc}")
            return
        raise
    badge = {"schemaVersion": 1, "label": "citations", "message": str(stats["citedby"])}
    STATS.write_text(json.dumps(stats, ensure_ascii=False), encoding="utf-8")
    BADGE.write_text(json.dumps(badge), encoding="utf-8")
    print(f"Read {len(stats['publications'])} publications and {stats['citedby']} citations from the public profile.")


if __name__ == "__main__":
    main()
