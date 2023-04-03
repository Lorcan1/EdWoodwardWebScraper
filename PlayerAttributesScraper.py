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

        player_info_df = pd.DataFrame([player_info])
        player_info_df.columns = player_info_df.iloc[0]
        player_info_df = player_info_df.drop(player_info_df.index[0])
        formatted_list = formatted_list[:len(formatted_list) - 4]
        player_info_df.loc[0] = formatted_list
        print(player_info_df)
        tables = soup.findChildren('table')
        stat_names = []
        stats = []
        for table in tables:
            rows = table.findChildren(['th', 'tr'])
            for row in rows:
                stat_names_regex = re.search('id="(.*)">', str(row))
                stat_regex = re.search('value_(.*)">', str(row))
                stat_names.append(stat_names_regex.group(1))
                stats.append(stat_regex.group(1))
        d = pd.DataFrame([stat_names])
        d.columns = d.iloc[0]
        d = d.drop(d.index[0])
        d.loc[0] = stats
        d = pd.concat([player_info_df,d], axis=1)
        d.head()
        # rename d, seperate out pandaframe header from rest as this doesnt
        # need to be scraped every time, split into functions




