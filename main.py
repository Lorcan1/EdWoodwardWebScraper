import requests
from bs4 import BeautifulSoup

def scrape():
    headers = {'User-Agent':
                   'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}
    page = "https://www.transfermarkt.co.uk/manchester-city/startseite/verein/281"
    html_text = requests.get(page, headers=headers)
    soup = BeautifulSoup(html_text.content, "html.parser")
    PlayersList = []
    Players = soup.find_all("img", {"class": "bilderrahmen-fixed lazy lazy"})
    for i in range(0,len(Players)):
        PlayersList.append(str(Players[i]).split('" class', 1)[0].split('<img alt="',1)[1])
    print(PlayersList)

if __name__ == '__main__':
    scrape()