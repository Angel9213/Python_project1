import requests
from bs4 import BeautifulSoup
import pandas as pd

# Set the URL of the Salary board index page
url = "https://www.ptt.cc/bbs/Salary/index.html"

# Set the User-Agent header to mimic a browser
headers = {"User-Agent":
           "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"}

# Send a GET request to the URL with the headers
response = requests.get(url, headers=headers)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Find all the article divs with the class "r-ent"
articles = soup.find_all("div",class_="r-ent")

# Create an empty list to store the article data
data_list = []

# Loop through each article div
for article in articles:
    # Create a dictionary to store the article data
    data = {}
    
    # Find the title div and extract the title text
    title = article.find("div", class_="title")
    if title and title.a:
        title = title.a.text
    else:
        title = "No Title"
    data["Title"] = title

    # Find the popularity div and extract the popularity text
    popular = article.find("div", class_="nrec")
    if popular and popular.span:
        popular = popular.span.text
    else:
        popular = "N/A"
    data["Popularity"] = popular

    # Find the date div and extract the date text
    date = article.find("div", class_="date")
    if date:
        date = date.text
    else:
        date = "N/A"
    data["Date"] = date

    # Append the article data to the data list
    data_list.append(data)

# Create a pandas DataFrame from the data list
df = pd.DataFrame(data_list)

# Save the DataFrame to an Excel file
df.to_excel("ptt_salary.xlsx", index=False)