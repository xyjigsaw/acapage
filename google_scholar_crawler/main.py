from scholarly import scholarly, ProxyGenerator
import json
from datetime import datetime
import os
import signal
import sys


RESULTS_DIR = "results"
GS_DATA_PATH = os.path.join(RESULTS_DIR, "gs_data.json")
SHIELDSIO_DATA_PATH = os.path.join(RESULTS_DIR, "gs_data_shieldsio.json")
FETCH_TIMEOUT_SECONDS = int(os.getenv("GOOGLE_SCHOLAR_TIMEOUT_SECONDS", "600"))


def raise_timeout(signum, frame):
    raise TimeoutError(f"Google Scholar update timed out after {FETCH_TIMEOUT_SECONDS} seconds")


def has_previous_results():
    return os.path.exists(GS_DATA_PATH) and os.path.exists(SHIELDSIO_DATA_PATH)


def fetch_author():
    pg = ProxyGenerator()
    pg.FreeProxies()  # Use free rotating proxies
    scholarly.use_proxy(pg)

    author: dict = scholarly.search_author_id(os.environ['GOOGLE_SCHOLAR_ID'])
    scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])
    author['updated'] = str(datetime.now())
    author['publications'] = {v['author_pub_id']: v for v in author['publications']}
    return author


try:
    signal.signal(signal.SIGALRM, raise_timeout)
    signal.alarm(FETCH_TIMEOUT_SECONDS)
    author = fetch_author()
except Exception as exc:
    if has_previous_results():
        print(f"Google Scholar update failed; keeping previous citation data: {exc}", file=sys.stderr)
        sys.exit(0)
    raise
finally:
    signal.alarm(0)

print(json.dumps(author, indent=2))
os.makedirs(RESULTS_DIR, exist_ok=True)
with open(GS_DATA_PATH, 'w') as outfile:
    json.dump(author, outfile, ensure_ascii=False)

shieldio_data = {
    "schemaVersion": 1,
    "label": "citations",
    "message": f"{author['citedby']}",
}
with open(SHIELDSIO_DATA_PATH, 'w') as outfile:
    json.dump(shieldio_data, outfile, ensure_ascii=False)
