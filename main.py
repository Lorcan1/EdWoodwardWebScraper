import requests
from bs4 import BeautifulSoup


def scrape():
    html_text = requests.get("https://www.premierleague.com/clubs/11/Manchester-City/squad").text
    with open(html_text) as fp:
        soup = BeautifulSoup(fp, "html.parser")


if __name__ == '__main__':
    scrape()


