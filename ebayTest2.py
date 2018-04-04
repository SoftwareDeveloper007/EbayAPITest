from urllib.request import urlopen
import json
import requests

with open("searches.txt", "r") as searchfile:
    searches = searchfile.readlines()
    print(searches)

for raw_item in searches:
    item = raw_item.strip().replace(" ", "+")
    key = 'MikeJohn-Search-PRD-578731904-721e4441'
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
&keywords=' + item)

    print("+-+-+-+-+-+- " + item + "+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+- ")

    apiResult = requests.get(url)
    parsedoc = apiResult.json()

    if parsedoc["findItemsByKeywordsResponse"][0]["searchResult"][0]["@count"] == "0":
        print("Not Found")
        continue
    for item in (parsedoc["findItemsByKeywordsResponse"][0]["searchResult"][0]["item"]):
        title = item["title"][0]
        condition = item["condition"][0]["conditionDisplayName"][0]
        price = item["sellingStatus"][0]["convertedCurrentPrice"][0]["__value__"]
        print(title + ", " + price + ", " + condition)
