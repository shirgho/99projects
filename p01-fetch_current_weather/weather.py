import urllib
import re
import json

wwo_apikey = "e6242d7fb7400876f8f047e897b4f5a2f61c7246"
wwo_weather_url = "http://api.worldweatheronline.com/free/v1/weather.ashx"

def findIP():
  url = "http://checkip.dyndns.org"
  query = urllib.urlopen(url).read()
  ipPattern = re.compile("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")
  ip = re.search(ipPattern,query)
  return ip.group()

myIP = findIP()

def queryWWO(api_url,ip):
  url = api_url + "?" + "key=" + wwo_apikey + "&q=" + ip + "&includeLocation=yes" + "&format=json"
  query = urllib.urlopen(url).read()
  return query

def parseWeather(data_json):
  weather = json.loads(data_json)
  weather_conditions = weather['data']['current_condition'][0].items()
  for item in weather_conditions:
    print('{key} : {value}'.format(key=item[0], value=item[1]))

parseWeather(queryWWO(wwo_weather_url,myIP))
