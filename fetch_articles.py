import json
import feedparser
from datetime import datetime

# RSS feeds mapping
RSS_FEEDS = {
    "Nature": "https://www.nature.com/nature.rss",
    "Cell": "https://www.cell.com/cell/current.rss",
    "Science": "https://www.science.org/action/showFeed?type=etoc&feed=rss&jc=science",
    "Nature Cell Biology": "https://www.nature.com/ncb.rss",
    "Developmental Cell": "https://www.cell.com/developmental-cell/current.rss",
    "The EMBO Journal": "https://www.embopress.org/action/showFeed?type=etoc&feed=rss&jc=embj",
    "Autophagy": "https://www.tandfonline.com/feed/rss/kaut20",
    "PNAS": "https://www.pnas.org/rss/current.xml",
    "Journal of Cell Biology": "https://rupress.org/jcb/rss/current.xml",
    "Molecular Cell": "https://www.cell.com/molecular-cell/current.rss",
    "Science Advances": "https://www.science.org/action/showFeed?type=etoc&feed=rss&jc=sciadv"
}

articles = []

for journal, rss_url in RSS_FEEDS.items():
    feed = feedparser.parse(rss_url)
    for entry in feed.entries[:5]:  # 每个期刊取前5篇
        articles.append({
            "title": entry.title,
            "journal": journal,
            "date": entry.get("published", ""),
            "url": entry.link
        })

# 按日期排序
articles.sort(key=lambda x: x["date"], reverse=True)

with open("articles.json", "w", encoding="utf-8") as f:
    json.dump({"items": articles}, f, indent=2, ensure_ascii=False)

print("articles.json updated.")
