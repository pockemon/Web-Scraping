from urllib.request import urlopen as Ureq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card'

# opening up connection, grabbing the page
Uclient = Ureq(my_url)

#it offloads the content into a variable
page_html = Uclient.read()

#close the connection
Uclient.close()

# html parsing
page_soup = soup(page_html, "html.parser")

# grabs each product
containers = page_soup.findAll("div", {"class": "item-container"})

for container in containers:
    brand = container.div.div.a.img["title"]
    
    title_container = container.findAll("a",{"class":"item-title"})
    product_name = title_container[0].text

    shipping_container = container.findAll("li",{"class":"price-ship"})
    shipping = shipping_container[0].text.strip()

    print("brand: " + brand)
    print("product_name: " + product_name)
    print("shipping: " + shipping)

 
