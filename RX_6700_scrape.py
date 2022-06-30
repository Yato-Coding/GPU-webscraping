import RTX_3070_scrape
from bs4 import BeautifulSoup
import requests
import re
from datetime import datetime


url = "https://www.alternate.de/listing.xhtml?q=AMD+RADEON+RX+6700+XT&s=default&filter_-2=true&filter_2203=AMD+Radeon+RX+6700+XT"

# Get Page
page = requests.get(url).text
document = BeautifulSoup(page, "html.parser")
items = document.find(class_="grid-container listing")


#Lists
links = []
names = []
prices = []
index_list = []


#Other Variables
continue_loop = True


#Get Link, Product Name and Price
for link in items.find_all("a", href=True):
    if link.text:
       links.append(link["href"])

for product_names in items.find_all("div", class_="product-name font-weight-bold"):
    names.append(product_names.text)

for price_tag in items.find_all(class_="price"):
    prices.append(price_tag.text)


number = len(names)


#Replace 
for x in range(number):
    prices[x] = int(prices[x].replace(",", "").replace(".", "").replace("€", "").replace("00", ""))
sorted_list = sorted(zip(prices, names, links))


x = 0


file = open("RX 6700 XT.txt", "w")
file.write(str(datetime.today()) + "\n")

while (continue_loop):
   if x != number:
       words = str(sorted_list[x]).split(",")


       print("-----------------------------------------------------------------------------------------")
       print(words[1])
       print(" " + words[0])
       print(words[3])
       print("-----------------------------------------------------------------------------------------")
       

       file.write("-----------------------------------------------------------------------------------------" + "\n")
       file.write(words[1] + "\n")
       file.write(words[0] + "\n")
       file.write(words[3] + "\n")


       x += 1

   else:
       continue_loop = False
       file.close()
