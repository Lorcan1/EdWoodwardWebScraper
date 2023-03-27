import requests
from bs4 import BeautifulSoup


class PlayerNameScraper:
    def player_name_scraper(self):
        headers = {'User-Agent':
                       'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}
        page = "https://www.transfermarkt.co.uk/manchester-city/startseite/verein/281"
        html_text = requests.get(page, headers=headers)
        soup = BeautifulSoup(html_text.content, "html.parser")
        players_list = []
        players = soup.find_all("img", {"class": "bilderrahmen-fixed lazy lazy"})
        for i in range(0,len(players)):
            players_list.append(str(players[i]).split('" class', 1)[0].split('<img alt="',1)[1])
        print(players_list)