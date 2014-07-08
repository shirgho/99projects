import requests
import bs4

BASE_URL = 'http://9gag.com/trending'

def connectSite(url):
    page = requests.get(url).text
    parsedPage = bs4.BeautifulSoup(page, 'lxml')
    return parsedPage

def getPostsUrls(parsedPage):
    links = parsedPage.find_all('article')
    postsUrls = list() 
    for link in links:
        postsUrls.append(link['data-entry-url'])
    return postsUrls

def getPostInfos(parsedPost):
    catchTitle = parsedPost.article.h2.contents[0]
    catchImage = parsedPost.article.img['src']
    return (catchTitle, catchImage)

def explorePostsUrls(postsUrls):
    indexLinks = list() 
    for url in postsUrls:
        page = connectSite(url.encode('utf-8'))
        infos = getPostInfos(page)
        indexLinks.append(infos)
    return indexLinks

def getData(url, max_tries = 5):
    tries = 0
    articles = None
    while articles is None and tries < max_tries:
        try:
            data = connectSite(url)
            links = getPostsUrls(data)
            articles = explorePostsUrls(links)
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
