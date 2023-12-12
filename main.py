####################
# AUHTOR : Neaje   #
####################

from bs4 import BeautifulSoup
import requests
from datetime import datetime
import time

def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()  
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "Error"

def parsePage(xml):
    soup = BeautifulSoup(xml, "xml") 
    items = soup.find_all('item')

    today = datetime.now().strftime("%a, %d %b %Y")

    for item in items:
        pubDate_tag = item.find('pubDate')
        pubDate_str = pubDate_tag.text.strip() if pubDate_tag else "N/A"

        pubDate = datetime.strptime(pubDate_str, "%a, %d %b %Y %H:%M:%S %z").strftime("%a, %d %b %Y")

        if pubDate == today:
            title = item.find('title').text.strip()
            link_tag = item.find('guid') 
            link = link_tag.text.strip() if link_tag else "N/A"
            description_tag = item.find('description')
            description = description_tag.text.strip() if description_tag else "N/A"

            print("Titre :", title)
            print("Lien :", link)
            print("Date :", pubDate_str)
            print("Description :", description)
            print("\n")

if __name__ == "__main__":
    url = "https://www.cert.ssi.gouv.fr/feed/"

    while True:
        xml = getHTMLText(url)
        parsePage(xml)
        time.sleep(3600)
