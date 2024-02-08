import feedparser
from datetime import datetime
from celery_tasks import classify_article
from database_module import store_article, DatabaseError

# List of RSS feed URLs
RSS_FEEDS = [
    'http://rss.cnn.com/rss/cnn_topstories.rss',
    'http://qz.com/feed',
    'http://feeds.foxnews.com/foxnews/politics',
    'http://feeds.reuters.com/reuters/businessNews',
    'http://feeds.feedburner.com/NewshourWorld',
    'https://feeds.bbci.co.uk/news/world/asia/india/rss.xml'
]

def extract_and_store_articles(feed_url):
    """
    Extract articles from the given RSS feed URL and store them in the database.
    """
    try:
        feed = feedparser.parse(feed_url)
        for entry in feed.entries:
            title = entry.title
            content = entry.get('summary', '')  # Some feeds might provide a summary
            publication_date = entry.published_parsed if 'published_parsed' in entry else datetime.now().timetuple()
            publication_date = datetime(*publication_date[:6]).strftime('%Y-%m-%d %H:%M:%S')
            source_url = entry.link
            store_article.delay(title, content, publication_date, source_url)
    except Exception as e:
        print(f"Error extracting articles from {feed_url}: {e}")

if __name__ == "__main__":
    for feed_url in RSS_FEEDS:
        extract_and_store_articles(feed_url)
