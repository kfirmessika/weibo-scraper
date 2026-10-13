// Weibo post details + comments via the kmscrape/weibo-scraper Apify Actor.
// npm install apify-client
// APIFY_TOKEN=... node example.mjs
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

const run = await client.actor('kmscrape/weibo-scraper').call({
    hotSearch: true,
    trendingPosts: true,
    includeComments: true,
    maxCommentsPerPost: 20,
    maxItemsPerSource: 20,
});

const { items } = await client.dataset(run.defaultDatasetId).listItems();
const byType = Object.groupBy(items, (i) => i.type);
for (const [type, rows] of Object.entries(byType)) console.log(type, rows.length);
console.log(byType.hot?.slice(0, 5));
