from urllib.request import urlopen
import json
import requests

# with open("searches.txt", "r") as searchfile:
#     searches = searchfile.readlines()
#     print(searches)

raw_item = "Philips"
item = raw_item.strip().replace(" ", "+")
key = 'PingZhan-AuctionE-PRD-b70a7e1cb-c8560761'
url = ('http://svcs.ebay.com/services/search/FindingService/v1?OPERATION-NAME=findCompletedItems\
&SERVICE-VERSION=1.7.0&SECURITY-APPNAME=' + key +
'&RESPONSE-DATA-FORMAT=JSON&REST-PAYLOAD&keywords=' + item +
'&itemFilter(0).name=FreeShippingOnly&itemFilter(0).value=true\
&itemFilter(1).name=SoldItemsOnly&itemFilter(1).value=true\
&itemFilter(2).name=MinPrice&itemFilter(2).value=400.0\
&itemFilter(3).paramName=Currency&itemFilter(3).paramValue=USD\
&sortOrder=PricePlusShippingLowest&paginationInput.entriesPerPage=100')

print("+-+-+-+-+-+- " + item + "+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+- ")

print(url)
apiResult = requests.get(url)
parsedoc = apiResult.json()

print(parsedoc)
#
# if parsedoc["findItemsByKeywordsResponse"][0]["searchResult"][0]["@count"] == "0":
#     print("Not Found")
# for item in (parsedoc["findItemsByKeywordsResponse"][0]["searchResult"][0]["item"]):
#     title = item["title"][0]
#     subtitle = item['subtitle'][0]
#     price = item["sellingStatus"][0]["convertedCurrentPrice"][0]["__value__"] + " " + \
#             item["sellingStatus"][0]["convertedCurrentPrice"][0]["@currencyId"]
#     item_id = item['itemId'][0]
#     categoryName = item['primaryCategory'][0]['categoryName'][0]
#     viewItemURL = item['viewItemURL'][0]
#
#     print(title + ", " + subtitle + ", " + categoryName + ", " + price + ", " + item_id + ", " + viewItemURL)
#
# """
#
# """
