from lxml import html
import csv, os, json
import requests
from exceptions import ValueError
from time import sleep


def ShopcluesParser(url):
	headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}
	page = requests.get(url, headers=headers)
	doc = html.fromstring(page.content)
	XPATH_NAME = '//h1[@itemprop="name"]//text()'
	XPATH_PRODUCTID = '//span[@class="pID"]//text()'
	XPATH_DISCOUNTED_PRICE = '//span[@class="f_price"]//text()'
	XPATH_SALE_PRICE = '//span[@id="sec_discounted_price_"]//text()'
	XPATH_ORIGINAL_PRICE = '//span[@id="sec_list_price_"]//text()'
	XPATH_DISCOUNT = '//span[@class="discount"]//text()'

	RAW_NAME = doc.xpath(XPATH_NAME)
	RAW_PRODUCTID = doc.xpath(XPATH_PRODUCTID)
	RAW_DISCOUNTED_PRICE = doc.xpath(XPATH_DISCOUNTED_PRICE)
	RAW_SALE_PRICE = doc.xpath(XPATH_SALE_PRICE)
	RAW_ORIGINAL_PRICE = doc.xpath(XPATH_ORIGINAL_PRICE)
	RAW_DISCOUNT = doc.xpath(XPATH_DISCOUNT)

	NAME = ' '.join(''.join(RAW_NAME).split()) if RAW_NAME else None
	PRODUCTID = ' '.join(''.join(RAW_PRODUCTID).split()).strip() if RAW_PRODUCTID else None
	DISCOUNTED_PRICE = ' '.join(''.join(RAW_DISCOUNTED_PRICE).split()).strip() if RAW_DISCOUNTED_PRICE else None
	SALE_PRICE = ' '.join(''.join(RAW_SALE_PRICE).split()).strip() if RAW_SALE_PRICE else None
	ORIGINAL_PRICE = ''.join(RAW_ORIGINAL_PRICE).strip() if RAW_ORIGINAL_PRICE else None
	DISCOUNT = ''.join(RAW_DISCOUNT).strip() if RAW_DISCOUNT else None

	if page.status_code != 200:
		raise ValueError('captha')
	data = {
            'NAME': NAME,
            'PRODUCTID': PRODUCTID,
            'DISCOUNTED_PRICE': DISCOUNTED_PRICE,
            'SALE_PRICE': SALE_PRICE,
            'ORIGINAL_PRICE': ORIGINAL_PRICE,
            'ORIGINAL_PRICE': ORIGINAL_PRICE,
            'DISCOUNT': DISCOUNT,
            'URL': url,
        }

	return data

def ReadAsin():
    # AsinList = csv.DictReader(open(os.path.join(os.path.dirname(__file__),"Asinfeed.csv")))
	genList = ['/footlodge-mens-casual-lace-up-shoes-309.html','/chevit-mens-stylish-112-blue-orange-wash-jeans-fashion-loafers-and-moccasins-shoes-casual-shoes-p-115123973.html']
	extracted_data = []
	for i in genList:
		url = "http://www.shopclues.com" + i
	print "Processing: "+url
	extracted_data.append(ShopcluesParser(url))
	sleep(5)
	f=open('mama.json','w')
	json.dump(extracted_data,f,indent=4)

if __name__ == "__main__":
	ReadAsin()

