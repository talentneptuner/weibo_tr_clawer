from urllib import parse
import datetime

class Properities():

    def __init__(self):
        self.params = {
            'q':parse.quote('宜宾地震'),
            'typeall':1,
            'suball':1
        }
        self.username = 'imtcsj@outlook.com'
        self.password = '19980910'

        self.start_year = 2019
        self.start_month = 6
        self.start_day = 17
        self.start_hour = 22
        self.end_year = 2019
        self.end_month = 6
        self.end_day = 20
        self.end_hour = 0
        self.urls = []
        self.timescopes = []
        self.get_timescope_list()

    def get_timescope_list(self):
        start_time_str = '{0}-{1}-{2}-{3}'.format(self.start_year, self.start_month,
                                                  self.start_day, self.start_hour)
        start_time = datetime.datetime.strptime(start_time_str,"%Y-%m-%d-%H")
        end_time_str = '{0}-{1}-{2}-{3}'.format(self.end_year, self.end_month,
                                                  self.end_day, self.end_hour)
        end_time = datetime.datetime.strptime(end_time_str, "%Y-%m-%d-%H")
        t = start_time
        while end_time.__gt__(t):
            temp = t + datetime.timedelta(hours=1)
            scope = t.strftime("%Y-%m-%d-%H") + ':' + temp.strftime("%Y-%m-%d-%H")
            self.timescopes.append(scope)
            self.urls.append('https://s.weibo.com/weibo?q={0}&typeall={1}&suball={2}&timescope=custom:{3}&Refer=g&page=1'
                              .format(self.params['q'], self.params['typeall'],
                                      self.params['suball'], scope))
            t = temp





