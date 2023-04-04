from PlayerAttributesScraper import PlayerAttributesScraper
from PlayerNameScraper import PlayerNameScraper

def fetch_hardcoded_outfield_player_list():
    return ["https://fminside.net/players/3-fm-23/28009441-kyle-walker",
            "https://fminside.net/players/3-fm-23/85085378-aymeric-laporte",
            "https://fminside.net/players/3-fm-23/55070299-ruben-dias",
            "https://fminside.net/players/3-fm-23/55041623-joao-cancelo",
            "https://fminside.net/players/3-fm-23/67217524-rodri",
            "https://fminside.net/players/3-fm-23/91003875-lkay-gundogan",
            "https://fminside.net/players/3-fm-23/18004457-kevin-de-bruyne",
            "https://fminside.net/players/3-fm-23/55041632-bernardo-silva",
            "https://fminside.net/players/3-fm-23/28067800-jack-grealish",
            "https://fminside.net/players/3-fm-23/29179241-erling-haaland"
            ]
def fetch_harcoded_goalkeeper_list():
    return ["https://fminside.net/players/3-fm-23/55057659-ederson",
            "https://fminside.net/players/3-fm-23/91100272-stefan-ortega"
            ]


if __name__ == '__main__':
    # player_name_scraper = PlayerNameScraper()
    # outfield_player_list, goalkeeper_list = player_name_scraper.player_name_scraper()
    #
    # outfield_player_list = outfield_player_list[:1]
    # goalkeeper_list = goalkeeper_list[:1]

    #scrape urls from this link https://fminside.net/clubs/3-fm-23/679-man-city eventually
    outfield_player_list = fetch_hardcoded_outfield_player_list()
    goalkeeper_list = fetch_harcoded_goalkeeper_list()


    player_attribute_scraper = PlayerAttributesScraper()
    outfield_player_information_df = player_attribute_scraper.player_attributes_scraper(outfield_player_list)
    goalkeeper_information_df = player_attribute_scraper.player_attributes_scraper(goalkeeper_list)

    outfield_player_information_df.to_csv(r'C:\Users\lorca\PycharmProjects\EdWoodwardScraper\outfield.csv')
    goalkeeper_information_df.to_csv(r"C:\Users\lorca\PycharmProjects\EdWoodwardScraper\goalkeeper.csv")
