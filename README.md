<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://i.imgur.com/6wj0hh6.jpg" alt="Project logo"></a>
</p>

<h3 align="center">Web Scraping Newegg</h3>

<div align="center">

  <img src="https://img.shields.io/badge/license-MIT-yellow.svg?style=flat-square">
  <img src="https://img.shields.io/badge/downloads-0k-yellow.svg?style=flat-square">
  <img src="https://img.shields.io/badge/build-passing-yellow.svg?style=flat-square">

</div>

---

<p align="center"> 
    <br> 
</p>



## 🧐 About <a name = "about"></a>

This is a web scraping program that harvest the website information and organize the prouct information in a sorted way. Everytime you run the program it will out put the updated information from the website


## Required Libraries
bs4
```
pip install beautifulsoup4
```

requests
```
python -m pip install requests
```

## 🏁 Installing

```
python3 web-scrape.py
```

## 🎈 Code Walk Through 
`uClient` is opening up a connection with the `my_url` and grabing the page information and store it in page_html

```python
my_url = "https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphic%20card"
#Opening up connection grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
```

Then we use soup to parse the html page and sotre it in `page_soup`. In order to know which div contains all of the products information, we need to inspect the web page and find the class name for that. In this case, we want to find all divs that have class name "item-container". containers is a list that contains all of the products info in this htnl page.

```python
uClient.close()
page_soup = soup(page_html, "html.parser")
containers = page_soup.findAll("div", {"class":"item-container"})
```
In the for loop, we are iterating over each individual item and check ther brand, title, and shipping info.

```python
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
```

## 🚀 Result 
![image](https://user-images.githubusercontent.com/32112516/62011746-e13d0380-b16b-11e9-9fbb-b42bdcf981b6.png)
![image](https://user-images.githubusercontent.com/32112516/62011758-fe71d200-b16b-11e9-95c0-4fbce377696d.png)

## ⛏️ Built Using <a name = "built_using"></a>
- [Python] - Programming Language

## License

🌱 MIT 🌱
