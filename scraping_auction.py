import requests
import bs4 as BeautifulSoup
from lxml import html

headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
url = "http://offer.ebay.co.uk/ws/eBayISAPI.dll?ViewBidsLogin&item=152699726936"

response = requests.get(url, headers=headers)
if response.status_code == 200:
    parser = html.fromstring(response.text)
    print(response.text)

    XPATH_LISTINGS = '/html/body/div[2]/div/div/div/table[2]/tbody/tr/td[1]/div[3]/div[2]/div/table[3]//tr'
    listings = parser.xpath(XPATH_LISTINGS)
    for i, row in enumerate(listings):
        if i==0:
            continue

        XPATH_USER_ID = 'td[2]/text()'
        XPATH_OFFER_PRICE = 'td[3]/text()'
        XPATH_OFFER_STATUS = 'td[4]/text()'
        XPATH_QUANTITY = 'td[5]/text()'
        XPATH_OFFER_DATE = 'td[6]/text()'

        raw_user_id = row.xpath(XPATH_USER_ID)
        raw_offer_price = row.xpath(XPATH_OFFER_PRICE)
        raw_offer_status = row.xpath(XPATH_OFFER_STATUS)
        raw_quantity = row.xpath(XPATH_QUANTITY)
        raw_offer_date = row.xpath(XPATH_OFFER_DATE)

        print(raw_user_id)
        print(raw_offer_price)
        print(raw_offer_status)
        print(raw_quantity)
        print(raw_offer_date)

