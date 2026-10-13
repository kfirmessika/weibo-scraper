# Weibo Scraper: Hot Search, Trending Posts, Comments & Profiles (no login)

Get **Weibo (微博) data as clean JSON** without a Weibo account, cookies or a Chinese phone number:

- **Hot search ranking (热搜榜)**: rank, keyword, heat score, label (热/新/沸) and category, refreshed live
- **Trending posts** by category (科技 Tech, 财经 Finance, 社会 Society, 娱乐 Entertainment, Sports, Gaming…)
- **Post details + comments** for any post URL or ID
- **User profiles** (followers, posts count, verification, bio)
- **Keyword suggestions** from Weibo search

It runs in the cloud as an Apify Actor: **[kmscrape/weibo-scraper](https://apify.com/kmscrape/weibo-scraper)**. You pay per result, there's no subscription, and Apify's free plan credits cover small runs.

## Who uses Weibo data

- **Brands & PR teams in China**: catch a trending complaint before it explodes (the #1 topic below is a franchise dispute).
- **Market & trend research**: what 500M+ Chinese users talk about today, by category.
- **Journalists / China watchers**: archive the hot search list hourly; topics often get censored and vanish.
- **Quant / sentiment**: heat score time series as a signal.

## Example output (real run, 2026-10-13)

```json
{
  "type": "hot",
  "rank": 1,
  "word": "霸王茶姬加盟商发声",
  "heat": 1131937,
  "label": "热",
  "category": "财经",
  "url": "https://s.weibo.com/weibo?q=%23%E9%9C%B8%E7%8E%8B%E8%8C%B6%E5%A7%AC%E5%8A%A0%E7%9B%9F%E5%95%86%E5%8F%91%E5%A3%B0%23",
  "scrapedAt": "2026-10-13T00:05:21.084Z"
}
```

More rows in [`sample_hot.json`](sample_hot.json).

## Quick start (no code)

1. Open **[Weibo Scraper on Apify](https://apify.com/kmscrape/weibo-scraper)** and click **Try for free**.
2. Tick what you want (hot search, trending posts, comments…) and press **Start**.
3. Download results as JSON, CSV or Excel, or connect Google Sheets, Zapier or Make.

## Python

```bash
pip install apify-client
```

```python
from apify_client import ApifyClient

client = ApifyClient("YOUR_APIFY_TOKEN")  # Apify Console → Settings → API & Integrations

run = client.actor("kmscrape/weibo-scraper").call(run_input={
    "hotSearch": True,
    "trendingPosts": True,
    "trendingCategoryIds": ["Technology", "Finance"],
    "maxItemsPerSource": 50,
})

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    if item["type"] == "hot":
        print(item["rank"], item["word"], item["heat"], item["category"])
```

Full script: [`example.py`](example.py)

## Node.js

```bash
npm install apify-client
```

```js
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
const run = await client.actor('kmscrape/weibo-scraper').call({
    hotSearch: true,
    postUrls: ['https://weibo.com/1234567890/AbCdEfGhI'],
    includeComments: true,
    maxCommentsPerPost: 50,
});
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(items);
```

Full script: [`example.mjs`](example.mjs)

## Monitor the hot search every hour

In Apify Console, open the Actor → **Schedule** → every hour. Each run's dataset is a timestamped snapshot of the ranking. Add a webhook or the Google Sheets integration to stream it wherever you need it.

## Input reference

| Field | What it does |
|---|---|
| `hotSearch` | Categorized hot search ranking |
| `trendingPosts` | Public posts from the trending feed |
| `trendingCategoryIds` | Categories: `科技`, `财经`, `Technology`, `Finance`, `Sports`, `Gaming`… or numeric IDs |
| `postUrls` | Post URLs or IDs for details + media |
| `includeComments` / `maxCommentsPerPost` | Public comments per post |
| `userUrls` | Profile URLs or numeric user IDs |
| `keywordSuggestions` | Keywords to expand via Weibo search suggestions |
| `maxItemsPerSource` | Cap per source |

## FAQ

**Do I need a Weibo account or cookies?** No. Only public data is collected.

**Does it work outside China?** Yes, it runs on Apify's cloud. Hot search has an automatic fallback endpoint when the main one times out from outside China.

**Keyword post search or a user's full timeline?** These need a logged-in Weibo session, so this Actor doesn't do them.

Questions or a field you need? [Open an issue](../../issues). I usually reply within a day.
