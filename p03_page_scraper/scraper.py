import requests
import re
import json

base_url = 'http://9gag.com/trending'

def connectSite(url):
    page = requests.get(url).text
    return page

def getLinks(page):
    linkPattern = re.compile('data-entry-url="(.*?)"')
    linkList = re.findall(linkPattern, page)
    return linkList

def parseLinks(page):
    titlePattern = re.compile('<h2 class="badge-item-title">(.*?)</h2>')
    imagePattern = re.compile('<link rel="image_src" href="(.*?)"')
    catchTitle = re.search(titlePattern, page)
    catchImage = re.search(imagePattern, page)
    return (catchTitle.group(1), catchImage.group(1))

def exploreLinks(linkList):
    indexArticle = 1
    indexLinks = dict() 
    for link in linkList:
        page = connectSite(link.encode('utf-8'))
        indexLinks[indexArticle] = parseLinks(page)
        print indexLinks[indexArticle]
        indexArticle += 1
    return indexLinks

def getData(url, max_tries = 5):
    tries = 0
    articles = None
    while articles is None and tries < max_tries:
        try:
            data = connectSite(base_url)
            links = getLinks(data)
            articles = exploreLinks(links)
        except Exception as error:
            print error
            tries += 1
    return articles

def genJson(articles):
    with open('indexedArticles.json', 'w') as articlesJson:
        json.dump(articles, articlesJson)
    return 'Articles indexed'

if __name__ == '__main__':
    articles = getData(base_url)
    genJson(articles)
