import requests
from bs4 import BeautifulSoup
import csv

url="https://books.toscrape.com/"

request_page=requests.get(url) # requesting the page to scrap data

page=BeautifulSoup(request_page.content,features="lxml") # converting the scraped data into Beautiful soup object to work with scraped data
# print(page.prettify()) # this will print the scraped contents in a nice indented form

products=page.find_all("article",attrs={"class":"product_pod"}) # this will return the list of products in the class=product_pod
print(products)

# lets take the single product
# product=page.find("article",attrs={"class":"product_pod"}) # this will return the first product in the class=product_pod

# title=product.h3.a["title"]
# print(f"Book Name: {title}")

# price=product.find(class_="price_color").text
# print(f"Book Price: {price}")

# rating=product.p["class"][1]
# print(f"Book Rating: {rating}")

# link=product.h3.a["href"]
# print(f"Purchase Link: {url+link}")

# availability=product.find(class_="instock availability").get_text()
# print(f"Book Availablility : {availability.strip()}")

# create seperate list for title,price,rating,link and availability to store the scraped data
title=list()
price=list()
rating=list()
link=list()
availability=list()

now scrap all the products and store it in the lists created
for product in products:
    title.append(product.h3.a["title"])
    price.append(product.find(class_="price_color").text)
    rating.append(product.p["class"][1])
    link.append(url+product.h3.a["href"])
    availability.append(product.find(class_="instock availability").get_text().strip())

print(f"List of Book Titles : {title}\n") # list of all book titles
print(f"List of Book Prices : {price}\n") # list of all book prices
print(f"List of all Book Ratings : {rating}\n")# list of all book rating
print(f"Availability of books : {availability}\n") # availability of books as list
print(f"List of all Books purshase links : {link}\n")  # list of all book purchasing links

# Lets convert the scraped data into the .csv file
# to work with or create csv file we need to import csv

csv_file=open("toscrape.csv","w")

csv_writer=csv.writer(csv_file)

csv_writer.writerow(rows) # rows for the csv file

for product in products:
    title=product.h3.a["title"]
    price=product.find(class_="price_color").text
    rating=product.p["class"][1]
    availability=product.find(class_="instock availability").get_text().strip()
    link=url+product.h3.a["href"]
    csv_writer.writerow([title,price,rating,availability,link])

csv_file.close()

# lets download the image using beautiful soup
image_link=page.find(class_="thumbnail")["src"]
image=url+image_link

# Request the link to download the image
img_data=requests.get(image).content

# Now create a file to store the scraped image
with open("A Light in the Attic.jpg","wb") as img: # wb means write binary the scraped content will be in binary form
    img.write(img_data)

# Now scrap the table in "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
link="https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
table_scrape=requests.get(link)
bs=BeautifulSoup(table_scrape.content,features="lxml")

# Lets take the single row
# table=bs.find(class_="table table-striped")
# print(table.prettify())

# e=table.tr.th.text
# print(e) #UPC

# e1=table.tr.td.text
# print(e1) #a897fe39b1053632

e=table.find_all("tr")
# print(e[0])
# print(e[0].th.text)
# print(e[0].td.text)

csv_table=open("table.csv","w")
csv_wr=csv.writer(csv_table)
csv_wr.writerow(["Label","Info"])

for i in e:
    label=i.th.text
    info=i.td.text
    csv_wr.writerow([label,info])
csv_table.close()

# now lets convert the scraped table into pandas DataFrame
import pandas as pd
table=bs.find(class_="table table-striped")
# print(table.prettify())

table_rows=table.find_all("tr")
# print(table_rows)

i=[]
j=[]

for table_row in table_rows:
    i.append(table_row.th.text)
    j.append(table_row.td.text)

# print(i)
# print(j)

p=pd.DataFrame({
    'index':i,
    'value':j
    })

print(p)
p.to_csv("table_df.csv")
