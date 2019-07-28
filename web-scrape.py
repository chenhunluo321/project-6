
from urllib.request import urlopen as uReq
# Parse the HTML
from bs4 import BeautifulSoup as soup

my_url = "https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphic%20card"
#Opening up connection grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")
# Grabs each product
containers = page_soup.findAll("div", {"class":"item-container"})




for container in containers:
	brand_container = container.findAll("a", {"class":"item-brand"})
	brand = brand_container[0].img["title"]
	title_container = container.findAll("a", {"class":"item-title"})
	product_name = title_container[0].text
	shipping_container = container.findAll("li", {"class":"price-ship"})
	shipping_price = shipping_container[0].text.strip()
	print("brand : ",brand)
	print("name : ",product_name)
	print("shipping price : ",shipping_price)
	print("--------------------")