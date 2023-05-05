from PlayerAttributesScraper import PlayerAttributesScraper
from PlayerUrlScraper import PlayerUrlScraper
from PlayersCleaner import PlayersCleaner


def fetch_hardcoded_all_player_list():
    return ["https://fminside.net/players/3-fm-23/28009441-kyle-walker",
            "https://fminside.net/players/3-fm-23/85085378-aymeric-laporte",
            "https://fminside.net/players/3-fm-23/55070299-ruben-dias",
            "https://fminside.net/players/3-fm-23/55041623-joao-cancelo",
            "https://fminside.net/players/3-fm-23/67217524-rodri",
            "https://fminside.net/players/3-fm-23/91003875-lkay-gundogan",
            "https://fminside.net/players/3-fm-23/18004457-kevin-de-bruyne",
            "https://fminside.net/players/3-fm-23/55041632-bernardo-silva",
            "https://fminside.net/players/3-fm-23/28067800-jack-grealish",
            "https://fminside.net/players/3-fm-23/29179241-erling-haaland",
            "https://fminside.net/players/3-fm-23/55057659-ederson",
            "https://fminside.net/players/3-fm-23/91100272-stefan-ortega"
            ]
def fetch_harcoded_goalkeeper_list():
    return ["https://fminside.net/players/3-fm-23/55057659-ederson",
            "https://fminside.net/players/3-fm-23/91100272-stefan-ortega"
            ]


if __name__ == '__main__':

    # outfield_player_list = outfield_player_list[:1]
    # goalkeeper_list = goalkeeper_list[:1]

    # player_url_scraper = PlayerUrlScraper()
    # list_of_urls = player_url_scraper.player_url_scraper()

    all_player_list = fetch_hardcoded_all_player_list()
    goalkeeper_list = fetch_harcoded_goalkeeper_list()

    #problem with gundogan, Stefan Ortega - sell value is added while contract end isnt
    player_attribute_scraper = PlayerAttributesScraper()
    outfield_player_information_df, goalkeeper_information_df = player_attribute_scraper.player_attributes_scraper(all_player_list)

    players_cleaner = PlayersCleaner()
    outfield_player_information_df = players_cleaner.clean(outfield_player_information_df)
    goalkeeper_information_df = players_cleaner.clean(goalkeeper_information_df)



    outfield_player_information_df.to_csv(r'C:\Users\lorca\PycharmProjects\EdWoodwardScraper\outfield.csv',index=False)
    goalkeeper_information_df.to_csv(r"C:\Users\lorca\PycharmProjects\EdWoodwardScraper\goalkeeper.csv",index=False)
