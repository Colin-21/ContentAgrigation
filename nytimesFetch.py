def getnyt(page = "Technology"):
    import requests
    import xml.etree.ElementTree as ET
    x = requests.get(f'https://rss.nytimes.com/services/xml/rss/nyt/{page}.xml')
    #x = requests.get('https://api.nytimes.com/svc/topstories/v2/technology.json?api-key=ywBfrbs8rFYJ2aEGdCqWHQSz0eZlXDix')

    root = ET.fromstring(x.text)
    articles = []
    for child in root.findall('./channel/item'):
        article = {}

        article['title'] = (child.find('title').text)
        article['description'] = (child.find('description').text)
        article['link'] = (child.find('link').text)
        article['pubDate'] = (child.find('pubDate').text)
        article['creator'] = (child.find('{http://purl.org/dc/elements/1.1/}creator').text)
        article['image'] = (child.find('{http://search.yahoo.com/mrss/}content').attrib['url'])
        articles.append(article)
    return articles
