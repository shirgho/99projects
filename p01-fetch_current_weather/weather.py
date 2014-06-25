import urllib
import re

ww_apikey = "e6242d7fb7400876f8f047e897b4f5a2f61c7246"
ww_weather_url = "http://api.worldweatheronline.com/free/v1/weather.ashx"
ww_city_url = "http://api.worldweatheronline.com/free/v1/search.ashx"

def findIP():
  url = "http://checkip.dyndns.org"
  query = urllib.urlopen(url).read()
  ipPattern = re.compile("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")
  ip = re.search(ipPattern,query)
  return ip.group()

myIP = findIP()

def queryWWO(api_url,ip):
  url = api_url + "?" + "key=" + ww_apikey + "&q=" + ip
  query = urllib.urlopen(url).read()
  return query

print(queryWWO(ww_city_url,myIP))
print(queryWWO(ww_weather_url,myIP))
