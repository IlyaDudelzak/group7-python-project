from django.shortcuts import render
import feedparser

# Create your views here.

NEWS_SOURCES = {
    "bbc": {
        "name": "BBC News",
        "url": "http://feeds.bbci.co.uk/news/rss.xml"
    },
    "cnn": {
        "name": "CNN",
        "url": "http://rss.cnn.com/rss/edition.rss"
    },
    "guardian": {
        "name": "The Guardian",
        "url": "https://www.theguardian.com/world/rss"
    },
}


def base_view(request):
    selected_source = request.GET.get("source", "bbc")
    query = request.GET.get("q", "")

    source = NEWS_SOURCES.get(selected_source, NEWS_SOURCES["bbc"])
    feed = feedparser.parse(source["url"])
    news = feed.entries[:10]

    if query:
        news = [item for item in news if query.lower() in item.title.lower()]

    return render(request, 'base.html', {
        "news": news,
        "query": query,
        "selected_source": selected_source,
        "sources": NEWS_SOURCES,
        "current_source": source,
    })
