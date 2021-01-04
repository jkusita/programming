# A program that gathers the current price of the stock FMETF.


# Find website with fmetf price
    # A: Bloomberg
# Gather data from said website:
    # Gather current price
    # Gather opening price
# Output data here

from lxml import html
import requests

#page = requests.get("https://www.bloomberg.com/quote/FMETF:PM")
page = requests.get("http://econpy.pythonanywhere.com/ex/001.html")
tree = html.fromstring(page.content)


# <span class="priceText__1853e8a5">108.0000</span>

# xpath: /html/body/div[2]/span
# original: <span class="item-price">$29.95</span> 
# book: //span[@class="item-price"]/text()

#closingPrice = tree.xpath("//span[@class="item-price"]/text()") # Why does this not work?
#closingPrice = tree.xpath('//span[@class="item-price"]/text()') # Why does this work?


# original: <span class="priceText__1853e8a5">108.0000</span>
# TODO: maybe we're not supposed to use /text() as it's a number? I'm not sure. 
closingPrice = tree.xpath('//span[@class="priceText__1853e8a5"]/text()')

print("helloWorld")
print(closingPrice)


# References:
    # https://docs.python-guide.org/scenarios/scrape/


