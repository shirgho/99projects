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
        print infos
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

def genIndex(articles):
    with open('indexedArticles.txt', 'a+') as indexTXT:
        lastIndexedArticle = ''
        for index, line in enumerate(indexTXT):
            if index == 1:
                lastIndexedArticle = line.strip()
                break
        for article in articles:
            if article[1] == lastIndexedArticle:
                print('Article already indexed, end of process')
                break
            indexTXT.write(article[0] + '\n' + article[1] + '\n\n')

if __name__ == '__main__':
    articles = getData(BASE_URL)
    genIndex(articles)
