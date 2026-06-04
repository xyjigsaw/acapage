from scholarly import scholarly, ProxyGenerator
import jsonpickle
import json
from datetime import datetime
import os
import sys


# Setup proxy
pg = ProxyGenerator()
try:
    pg.FreeProxies()  # Use free rotating proxies
    scholarly.use_proxy(pg)
except TypeError as exc:
    # Some free-proxy releases changed get_proxy_list(repeat), which breaks
    # scholarly's FreeProxies integration when dependency resolution drifts.
    print(f"Free proxy setup failed, continuing without proxy: {exc}", file=sys.stderr)
except Exception as exc:
    print(f"Free proxy setup failed, continuing without proxy: {exc}", file=sys.stderr)

author: dict = scholarly.search_author_id(os.environ['GOOGLE_SCHOLAR_ID'])
scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])
name = author['name']
author['updated'] = str(datetime.now())
author['publications'] = {v['author_pub_id']:v for v in author['publications']}
print(json.dumps(author, indent=2))
os.makedirs('results', exist_ok=True)
with open(f'results/gs_data.json', 'w') as outfile:
    json.dump(author, outfile, ensure_ascii=False)

shieldio_data = {
  "schemaVersion": 1,
  "label": "citations",
  "message": f"{author['citedby']}",
}
with open(f'results/gs_data_shieldsio.json', 'w') as outfile:
    json.dump(shieldio_data, outfile, ensure_ascii=False)
