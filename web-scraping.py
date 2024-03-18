from bs4 import BeautifulSoup
import requests

page_to_scrape = requests.get("https://www.scrapethissite.com/pages/")
soup = BeautifulSoup(page_to_scrape.text, "html.parser")
titles = soup.findAll(attrs={"class": "page-title"})
descriptions = soup.findAll(attrs={"class": "session-desc"})

for title,description in zip(titles,descriptions):
    print(title.text + "description: " + description.text)