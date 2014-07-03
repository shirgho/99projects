import urllib2
import re
import json

base_url = 'http://9gag.com/trending'

def connectSite(url):
    page = urllib2.urlopen(url).read()
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
        page = connectSite(link)
        indexLinks[indexArticle] = parseLinks(page)
        indexArticle += 1
    return indexLinks

if __name__ == '__main__':
    links = getLinks(connectSite(base_url))
    articles = exploreLinks(links)
    with open('indexedArticles.txt', 'w') as articlesJson:
        json.dump(articles, articlesJson)
