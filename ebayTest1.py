from urllib.request import urlopen
import json
import requests

search_term = "ES-2620"
key = 'PingZhan-AuctionE-PRD-b70a7e1cb-c8560761'
url = ('http://svcs.ebay.com/services/search/FindingService/v1\
?OPERATION-NAME=findItemsByKeywords\
&SERVICE-VERSION=1.0.0\
&SECURITY-APPNAME=' + key +
'&RESPONSE-DATA-FORMAT=JSON\
&REST-PAYLOAD\
&itemFilter(0).name=Condition\
&itemFilter(0).value=New\
&itemFilter(1).name=MaxPrice\
&itemFilter(1).value=500.0\
&itemFilter(1).paramName=Currency\
&itemFilter(1).paramValue=USD\
&keywords=' + search_term)

print(url)

apiResult = requests.get(url)
parsedoc = apiResult.json()
print(parsedoc)
for item in (parsedoc["findItemsByKeywordsResponse"][0]["searchResult"][0]["item"]):
    title = item["title"][0]
    condition = item["condition"][0]["conditionDisplayName"][0]
    price = item["sellingStatus"][0]["convertedCurrentPrice"][0]["__value__"]
    print(title + ", " + price + ", " + condition)