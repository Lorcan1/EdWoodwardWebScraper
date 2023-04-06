import requests
from bs4 import BeautifulSoup


class PlayerUrlScraper:
    def player_url_scraper(self):
        headers = {'User-Agent':
                       'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}
        url = "https://fminside.net/clubs/3-fm-23/679-man-city"
        html_text = requests.get(url, headers=headers)
        soup = BeautifulSoup(html_text.content, "html.parser")
        tables = soup.findAll("div", {"id": "player_table"})
        list_of_urls = []
        for table in tables:
            if table.h2.contents[0] == 'Full Squad':
                for a in soup.find_all('a', href=True):
                    if '/players/3' in a['href']:
                        list_of_urls.append(a['href'])
        return list_of_urls



if __name__ == '__main__':
    p = PlayerUrlScraper()
    p.player_url_scraper()
