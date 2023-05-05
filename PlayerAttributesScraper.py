import re
import requests
from bs4 import BeautifulSoup, NavigableString, Tag
import pandas as pd


class PlayerAttributesScraper:
    def player_attributes_scraper(self, names_list):
        is_first_outfield_player = True
        is_first_goalkeeper = True
        outfield_players = pd.DataFrame()
        goalkeepers = pd.DataFrame()
        for name in names_list:
            url = self.url_creator(name)
            soup = self.soup_creator(url)
            if is_first_outfield_player or is_first_goalkeeper:
                personal_info_df = self.get_personal_info(soup,True)
                attribute_info_df = self.get_attribute_info(soup,True)
                if personal_info_df['Position'].str.contains('GK').any() and is_first_goalkeeper is True:
                    goalkeepers = pd.concat([personal_info_df, attribute_info_df], axis=1)
                    is_first_goalkeeper = False
                elif is_first_outfield_player:
                    outfield_players = pd.concat([personal_info_df, attribute_info_df], axis=1)
                    is_first_outfield_player = False
                else:
                    goalkeepers, outfield_players = self.append_to_df(soup,goalkeepers,outfield_players)

            else:
                goalkeepers, outfield_players = self.append_to_df(soup, goalkeepers, outfield_players)
                # personal_info_stats = self.get_personal_info(soup,True)
                # attribute_info_stats = self.get_attribute_info(soup,True)
                # personal_info_stats.extend(attribute_info_stats)
                # if 'GK' in personal_info_stats:
                #     goalkeepers.loc[len(goalkeepers)] = personal_info_stats
                # else:
                #     outfield_players.loc[len(outfield_players)] = personal_info_stats

        return outfield_players,goalkeepers

    def url_creator(self,name): #to be completed
        return name
        # if name == 1:
        #     return "https://fminside.net/players/3-fm-23/55070299-ruben-dias"
        # elif name == 2:
        #     return "https://fminside.net/players/3-fm-23/55057659-ederson"
        # # else:
        #     return "https://fminside.net/players/2-fm-22/55070299-ruben-dias"

    def soup_creator(self,url):
        headers = {'User-Agent':
                       'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}
        html_text = requests.get(url, headers=headers)
        return BeautifulSoup(html_text.content, "html.parser")

    def get_personal_info(self,soup,is_first_player):
        original_personal_info = soup.findAll(class_="value")
        info_list = []
        for info in original_personal_info:
            if info.i and info.i.get_text() == "Not for sale":
                info_list.append(info.i.get_text())
            info_list.append(info.contents[0])

        formatted_list = []
        for i in range(0, len(info_list) - 1):  # split into seperate function
            if isinstance(info_list[i], NavigableString) or isinstance(info_list[i], str):
                formatted_list.append(info_list[i])
            else:
                if i == 2:
                    try:
                        x = re.split("</a>", str(info_list[i]))
                        y = re.split('"/>', x[0])
                        if len(y) > 1:
                            z = y[1]
                    except AttributeError:
                        pass
                if i == 5:
                    x = re.split("</span>", str(info_list[i]))
                    y = re.split('">', x[0])
                    z = y[2]
                    formatted_list.append(z)

        formatted_list = formatted_list[0:12]
        overall, potential = self.return_overall_potential(soup)
        formatted_list.append(overall)
        formatted_list.append(potential)
        if is_first_player:
            player_info = ['Club', 'Name', 'Age', 'Position', 'Foot', 'Height', 'Weight', 'Caps/ Goals', 'Unique ID',
                           'Sell Value', 'Wages', 'Contract End', 'Overall', 'Potential']

            personal_info_df = pd.DataFrame([player_info])
            personal_info_df.columns = personal_info_df.iloc[0]
            player_info_df = personal_info_df.drop(personal_info_df.index[0])
            player_info_df.loc[0] = formatted_list
            return player_info_df
        else:
            return formatted_list

    def get_attribute_info(self,soup,is_first_player):
        tables = soup.findChildren('table')
        stat_names = []
        stats = []
        for table in tables:
            rows = table.findChildren(['th', 'tr'])
            for row in rows:
                if is_first_player:
                    stat_names_regex = re.search('id="(.*)">', str(row))
                    stat_names.append(stat_names_regex.group(1))
                stat_regex = re.search('value_(.*)">', str(row))
                stats.append(stat_regex.group(1))
        if is_first_player:
            attributes_info_df = pd.DataFrame([stat_names])
            attributes_info_df.columns = attributes_info_df.iloc[0]
            attributes_info_df = attributes_info_df.drop(attributes_info_df.index[0])
            attributes_info_df.loc[0] = stats
            return attributes_info_df
        else:
            return stats

    def return_overall_potential(self,soup):
        overall = soup.select_one("span[id*=ability]").text
        potential = soup.select_one("span[id*=potential]").text
        return overall, potential

    def append_to_df(self,soup,goalkeepers,outfield_players):
        personal_info_stats = self.get_personal_info(soup, False)
        attribute_info_stats = self.get_attribute_info(soup, False)
        personal_info_stats.extend(attribute_info_stats)
        if 'GK' in personal_info_stats:
            goalkeepers.loc[len(goalkeepers)] = personal_info_stats
        else:
            outfield_players.loc[len(outfield_players)] = personal_info_stats
        return goalkeepers,outfield_players

