import requests
import re
import json

BASE_URL = 'http://9gag.com/trending'

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
    indexLinks = list() 
    for link in linkList:
        page = connectSite(link.encode('utf-8'))
        infos = parseLinks(page)
        indexLinks.append(infos)
    return indexLinks

def getData(url, max_tries = 5):
    tries = 0
    articles = None
    while articles is None and tries < max_tries:
        try:
            data = connectSite(url)
            links = getLinks(data)
            articles = exploreLinks(links)
        except Exception as error:
            print error
            tries += 1
    return articles

def spotDuplicates(articles):
    with open('indexedArticles.txt', 'r') as indexTXT:
        data = indexTXT.readlines()
        indexDuplicate = len(articles)
        try:
            lastUrlImage = data[-2].strip()
            for article in articles:
                url_image = article[1].encode('ascii','ignore')
                if url_image == lastUrlImage:
                    indexDuplicate = articles.index(article)
                    print 'duplicates spotted and eliminated'
        except IndexError:
            print 'indexedArticles.txt empty, creating it'
        return indexDuplicate
            

def genIndex(articles):
    with open('indexedArticles.txt', 'a+') as indexTXT:
        indexDuplicate = spotDuplicates(articles)
        for article in reversed(articles[:indexDuplicate]):
            title_article, url_image = article
            indexTXT.write(title_article + '\n' + url_image + '\n\n')
    print 'indexing completed'

if __name__ == '__main__':
    articles = getData(BASE_URL)
    genIndex(articles)
