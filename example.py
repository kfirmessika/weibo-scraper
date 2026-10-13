"""Weibo hot search + trending posts via the kmscrape/weibo-scraper Apify Actor.

pip install apify-client
APIFY_TOKEN=... python example.py
"""
import csv
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run = client.actor("kmscrape/weibo-scraper").call(run_input={
    "hotSearch": True,
    "trendingPosts": True,
    "trendingCategoryIds": ["Technology", "Finance"],
    "maxItemsPerSource": 50,
})

rows = list(client.dataset(run["defaultDatasetId"]).iterate_items())
hot = [r for r in rows if r.get("type") == "hot"]

for r in hot[:10]:
    print(f"#{r['rank']:>2}  {r['word']}  heat={r['heat']:,}  [{r.get('category')}]")

with open("weibo_hot.csv", "w", newline="", encoding="utf-8-sig") as f:
    w = csv.DictWriter(f, fieldnames=["rank", "word", "heat", "label", "category", "url", "scrapedAt"], extrasaction="ignore")
    w.writeheader()
    w.writerows(hot)
print(f"saved {len(hot)} hot search rows to weibo_hot.csv")
