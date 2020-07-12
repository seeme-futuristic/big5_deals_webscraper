from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


my_url = 'https://www.big5sportinggoods.com/store/browse/_/N-aZ2Z3'

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")


containers = page_soup.findAll("div", {"class":"product-tile"})

#print(len(containers)) ~this tells me how many products/items are on a page


filename = "big_5_deals.csv"
f = open(filename, "w")

headers = "name_of_item, price\n"

f.write(headers)


for container in containers:

    title_container = container.find("div", {"class":"product_name"})
    name_of_item = container.div.div.a.text


    node = container.find("div", {"class":"regular-price"})
    if node is not None:
        original_price = container.find("div", {"class":"regular-price"}).text
        print(original_price)
    else:
        sale_price = container.find("div", {"class":"sale-price"}).text
        print(sale_price)

        price = sale_price



        f.write(name_of_item.replace(",", "|") + "," + price + "\n")


f.close()
