import requests
from bs4 import BeautifulSoup
import os

def download_img(url, save_path):
    print(f"Downloading image: {url}")
    response = requests.get(url)
    if response.status_code == 200:  # Ensure the request was successful
        with open(save_path, "wb") as file:
            file.write(response.content)
        print(f"Image has been downloaded to: {save_path}")
        print("-" * 30)
    else:
        print(f"Download failed, status code: {response.status_code}")

def main():
    url = "https://www.ptt.cc/bbs/Beauty/M.1686997472.A.FDA.html"
    headers = {"Cookie": "over18=1"}
    
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Unable to access the webpage, status code: {response.status_code}")
        return

    soup = BeautifulSoup(response.text, "html.parser")
    spans = soup.find_all("span", class_="article-meta-value")

    if len(spans) < 3:
        print("Unable to retrieve the article title")
        return

    title = spans[2].text.strip()  # Get the title and remove whitespace

    # Create a folder for images 📁
    dir_name = f"images/{title}"
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

    # Find all image links on the webpage
    links = soup.find_all("a")
    allow_file_name = ["jpg", "png", "jpeg", "gif"]
    for link in links:
        href = link.get("href")
        if not href:
            continue
        
        if not href.startswith("http"):  # Ensure it is a complete URL
            continue

        file_name = href.split("/")[-1]
        extension = file_name.split(".")[-1].lower() if "." in file_name else ""
        
        if extension in allow_file_name:
            print(f"File format: {extension}")
            print(f"URL: {href}")
            download_img(href, f"{dir_name}/{file_name}")

if __name__ == "__main__":
    main()