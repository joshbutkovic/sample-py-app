import requests
import urllib.request
import time
from bs4 import BeautifulSoup


class Cli:

    def __init__(self):
        self.options = ['NFL', 'NBA', 'MLB']

    def start(self):
        print("\nChoose a sport:")
        self.show_options()
        self.get_choice()

    def show_options(self):
        for i, option in enumerate(self.options, start=1):
            print(f"{i}) {option}")

    def get_choice(self):
        choice = input()
        print(f"Your choice was: {choice}\nProcessing...")
        self.process_choice()

    def process_choice(self):
        url = 'http://www.nfl.com/stats/categorystats?tabSeq=2&defensiveStatisticCategory=GAME_STATS&conference=ALL&role=OPP&season=2019&seasonType=REG&d-447263-s=TOTAL_YARDS_GAME_AVG&d-447263-o=1&d-447263-n=1'
        response = requests.get(url)
        # print(response.text)
        soup = BeautifulSoup(response.text, "html.parser")
        soup_table = soup.find_all('table')
        print(soup_table)
        # time.sleep(1)
        # print(soup.find_all('a'))
