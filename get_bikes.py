from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup as soup
import requests

my_url = 'https://www.ebay-kleinanzeigen.de/s-fahrraeder/kaiserslautern/c217l5466r10'
req = Request(my_url, headers={'User-Agent': 'Mozilla/5.0'})   # headers, damit webseite geöffnet wird, sons error 404

# open connection and grabbing the page
html_text = urlopen(req).read()
# print(page_html)

# page_soup = soup(page_html, "html.parser")
soup = soup(html_text, "lxml")

# match = soup.find(id='srchrslt-adtable', class_='itemlist-separatedbefore ad-list lazyload')

match_all = soup.find_all('li', class_='ad-listitem lazyload-item')

counter = 1

for full_line in match_all: 
	try:

		titel_found = full_line.find(class_='aditem-main')
		titel = titel_found.a.string

		image_found = full_line.find(class_='imagebox srpimagebox')
		image_link = image_found.get('data-imgsrc')

		details_found = full_line.find(class_='aditem-details')
		price = details_found.strong.string

		full_link = full_line.find(class_='ellipsis')
		full_link = 'https://www.ebay-kleinanzeigen.de' + full_link.get('href')

		req = requests.get(image_link)

		img_name = "img/" + str(counter) + ".jpg"

		with open(img_name, "wb") as f:
			f.write(req.content)
			counter += 1
		
		print(titel + ', ' + price)
		print(full_link)
		print(4*'####')
	except:
		pass


# you grabbing header (h1) from webpage
# print(soup.prettify())
