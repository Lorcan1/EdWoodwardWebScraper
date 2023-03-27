import re
import requests
from bs4 import BeautifulSoup, NavigableString, Tag
import pandas as pd


class PlayerAttributesScraper:
    def player_attributes_scraper(self, names_list):
        headers = {'User-Agent':
                       'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}
        page = "https://fminside.net/players/2-fm-22/85085378-aymeric-laporte"
        html_text = requests.get(page, headers=headers)
        soup = BeautifulSoup(html_text.content, "html.parser")
        # print(soup.prettify())
        original_personal_info = soup.findAll(class_="value")
        info_list = []
        for info in original_personal_info:
            info_list.append(info.contents[0])

        formatted_list = []
        for i in range(0,len(info_list)-1):  # split into seperate function
            if isinstance(info_list[i], NavigableString):
                formatted_list.append(info_list[i])
            else:
                if i == 2:
                     try:
                         x= re.split("</a>", str(info_list[i]))
                         y = re.split('"/>',x[0])
                         if len(y) > 1:
                            z = y[1]
                     except AttributeError:
                         pass
                if i == 5:
                    x = re.split("</span>", str(info_list[i]))
                    y = re.split('">', x[0])
                    z = y[2]
                    formatted_list.append(z)

        player_info = ['Club','Name', 'Age','Position','Foot','Height','Weight', 'Caps/ Goals', 'Unique ID','Sell Value','Wages', 'Contract End']

        df = pd.DataFrame(formatted_list, columns=['Player'])
        df = df.iloc[:-4] # last 4 rows are not relevant 'best suitable roles'
        df.insert(0, "Player Info", player_info)
        print(df)