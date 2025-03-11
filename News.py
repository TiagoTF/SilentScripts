import webbrowser
import feedparser

def main():
    website_list = "https://feeds.feedburner.com/TheHackersNews"

    NewsFeed = feedparser.parse(website_list)
    print(NewsFeed.entries)
    article_list = []
    article_link = []
    for i in range(5):
        article = NewsFeed.entries[i]
        titles = article.title
        link = article.link
        article_link.append(link)
        article_list.append(titles)

    article_num=1
    for article in article_link:
        webbrowser.open(article)

main()