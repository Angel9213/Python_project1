import requests
from bs4 import BeautifulSoup
import pandas as pd

current_page = 1

data = []

proceed = True

while current_page <= 2:
    print("Currently scraping page:" + str(current_page))

    url ="https://books.toscrape.com/catalogue/page-"+str(current_page)+".html"
    
    page = requests.get(url)
    
    soup = BeautifulSoup(page.text,"html.parser")

    if soup.title.text == "404 Not Found":
        break

    else:
        all_books = soup.find_all("li", class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")
        
        for book in all_books:
            item = {}
            
            item["Title"] = book.find("img").attrs["alt"]
            
            item["Link"] = "https://books.toscrape.com/catalogue/"+book.find("a").attrs["href"]
            
            item["Price"] = book.find("p", class_="price_color").text[2:]
            
            item["Stock"] = book.find("p", class_="instock availability").text.strip()
            
            data.append(item)

            
        
    current_page += 1

for item in data:
    print(f"Title:{item["Title"]}")
    print(f"Link:{item["Link"]}")
    print(f"Stock:{item["Stock"]}")
    print(f"Price:{item["Price"]}")
    print()

    
df = pd.DataFrame(data)
df.to_excel("books.xlsx", index=False)
df.to_csv("books.csv",index=False)




