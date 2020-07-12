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

headers = "name_of_item, price, saving?\n"

f.write(headers)


for container in containers:

    name_of_item = container.div.div.a.text

    sale_price = container.find("div", {"class":"product-details-container-bottom"}).div.div.text

    price_container = container.find("div", {"class":"product-details-container-bottom"})
    if price_container.find("div", {"class":"savings"}) is not None:
        saving_ = print("YES")
        a_string = "YES" if saving_ is None else saving_
        print(a_string)

    else:
        saving_ = print("NO")
        a_string = "NO" if saving_ is None else saving_
        print(a_string)


    f.write(name_of_item + "," + sale_price + "," + a_string + "\n")

f.close()
