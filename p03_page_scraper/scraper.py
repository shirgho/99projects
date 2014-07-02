import urllib
import re

base_url = 'http://9gag.com/trending'

def connectSite(url):
    page = urllib.urlopen(url).read()
    return page

def getLinks(page):
    linkPattern = re.compile('src="(.*?.jpg|.*?.png|.*?.gif)"')
    linkList = re.findall(linkPattern, page)
    return linkList

if __name__ == '__main__':
    links = getLinks(connectSite(base_url))
    for link in links:
        print link
