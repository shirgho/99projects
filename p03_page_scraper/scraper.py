import urllib
import re

base_url = 'http://9gag.com/trending'

def connectSite(url):
    page = urllib.urlopen(url).read()
    return page

def getArticles(page):
    articlePattern = re.compile('<header.*?>(.*?)</header>', re.DOTALL)
    articleList = re.findall(articlePattern, page)
    return articleList[2]

if __name__ == '__main__':
    print getArticles(connectSite(base_url))
