from urllib import request as re
import requests

class Downloader():
    def __init__(self, url, session):
        self.url = url
        self.headers_ = {'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                                     "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}
        # req = re.Request(url, headers=self.headers_)
        # res = re.urlopen(req, timeout=30)
        # self.code = res.getcode()
        # self.text = str(res.read())

        res = session.get(url)
        self.text = res.text

    def get_text(self):
        return self.text
