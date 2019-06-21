from bs4 import BeautifulSoup
from downloader import Downloader
from weiboParser import weiboParser
from weiboTrParser import weiboTroutParser

class pageParser():
    def __init__(self, downloader:Downloader):
        self.downloader_ = downloader
        self.soup_ = BeautifulSoup(downloader.text, 'html.parser', from_encoding='utf-8')
        self.info = []
        self.trans_info = []
        self.get_card()
        self.get_all_info()
        self.is_last()

    def is_last(self):
        is_last = self.soup_.find_all('div', class_='card-no-result')
        if is_last:
            self.is_last = 1
        else:
            self.is_last = 0

    def get_card(self):
        self.blocks_ = self.soup_.find_all('div', class_="card-wrap")

    def get_all_info(self):
        for block in self.blocks_:
            check_temp = BeautifulSoup(str(block), 'html.parser')
            has_tr = check_temp.find_all('div', class_='card-comment')
            if has_tr:
                weibo_parser = weiboTroutParser(block)
                if weibo_parser.info['mid']:
                    self.info.append(list(weibo_parser.info.values()))
                    self.trans_info.append(list(weibo_parser.get_tr_info().values()))
            else:
                weibo_parser = weiboParser(block)
                if weibo_parser.info['mid']:
                    self.info.append(list(weibo_parser.info.values()))


