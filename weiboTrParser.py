from bs4 import BeautifulSoup
import datetime
import re


class weiboTrinParser():

    def __init__(self, block):
        self.block_ = block
        self.info = {}
        self.soup_ = BeautifulSoup(str(block), 'html.parser')
        self.info['mid'] = self.get_mid()
        self.info['nick_name'] = self.get_userinfo()[0]
        self.info['url'] = self.get_userinfo()[1]
        self.info['u_id'] = self.get_userinfo()[2]
        self.info['text'] = self.get_text()
        self.info['location'] = self.get_location()
        self.info['img_list'] = self.get_imglist()
        self.info['time'] = self.get_time_device()[0]
        self.info['device'] = self.get_time_device()[1]
        self.info['transmit_num'] = self.get_nums()[0]
        self.info['comment_num'] = self.get_nums()[1]
        self.info['like_num'] = self.get_nums()[2]
        self.info['now_time'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        self.info['trans'] = ''

    def get_mid(self):
        try:
            mid = self.soup_.find('a', attrs={'action-data': True, 'title': '赞'})
            return mid.attrs['action-data'].replace('mid=', '')
        except:
            return ''

    def get_userinfo(self):
        try:
            nickNameSoup = self.soup_.find('a', class_='name')
            nick_name = nickNameSoup.get_text()
            url = nickNameSoup.attrs['href']
            u_id = url.replace('//weibo.com/u/', '')
            return nick_name, url, u_id
        except:
            return '', '', ''

    def get_imglist(self):
        try:
            img_content = self.soup_.find('div', class_='media media-piclist')
            img_soup = BeautifulSoup(str(img_content), 'html.parser')
            img_list = img_soup.find_all('img')
            return '|'.join([img['src'] for img in img_list])
        except:
            return ''

    def get_text(self):
        try:
            outTxt = self.soup_.find_all('p', class_='txt')
            text =  str(outTxt[-1].get_text()).strip().replace('收起全文d', '')
            return text
        except:
            return ''

    def get_location(self):
        try:
            pattern = '<a href="http://t.cn/[\S\s]*?</a>'
            results = re.findall(pattern, str(self.block_))
            for result in results:
                if '<i class="wbicon">2</i>' in result:
                    soup_temp = BeautifulSoup(str(result), 'html.parser')
                    location_text = soup_temp.find('a')
                    location = location_text.get_text()
                    return location.replace('2', '')
            return ''

        except:
            return ''

    def get_time_device(self):
        try:
            pList = self.soup_.find_all('p', class_='from')[-1]
            soupTemp = BeautifulSoup(str(pList), 'html.parser')
            try:
                time = soupTemp.find_all('a')[0].get_text().replace('\n','').strip()
            except:
                time = ''
            try:
                device = soupTemp.find_all('a')[1].get_text().replace('\n','').strip()
            except:
                device = ''
            return time, device
        except:
            return '', ''

    def get_nums(self):
        try:
            liList = self.soup_.find('div', class_='func')
            soupTemp = BeautifulSoup(str(liList), 'html.parser')
            actList = soupTemp.find_all('li')
            transmitNum = str(actList[0].get_text()).replace('转发', '')
            commentNum = str(actList[1].get_text()).replace('评论', '')
            likeNum = str(BeautifulSoup(str(actList[2]), 'html.parser').find('em').get_text())
            if transmitNum.strip() == '':
                transmitNum = 0
            if commentNum.strip() == '':
                commentNum = 0
            if likeNum.strip() == '':
                likeNum = 0
            return int(transmitNum), int(commentNum), int(likeNum)
        except:
            return 0, 0, 0

class weiboTroutParser():
    def __init__(self, block):
        self.block_ = block
        self.info = {}
        self.soup_ = BeautifulSoup(str(block), 'html.parser')
        self.info['mid'] = self.get_mid()
        self.info['nick_name'] = self.get_userinfo()[0]
        self.info['url'] = self.get_userinfo()[1]
        self.info['u_id'] = self.get_userinfo()[2]
        self.info['text'] = self.get_text()
        self.info['location'] = self.get_location()
        self.info['img_list'] = ''
        self.info['time'] = self.get_time_device()[0]
        self.info['device'] = self.get_time_device()[1]
        self.info['transmit_num'] = self.get_nums()[0]
        self.info['comment_num'] = self.get_nums()[1]
        self.info['like_num'] = self.get_nums()[2]
        self.info['now_time'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        self.tr_info = self.get_tr_info()
        self.info['trans'] = self.tr_info['mid']

    def get_mid(self):
        try:
            mid = self.soup_.find('div', attrs={'mid': True})
            return mid.attrs['mid']
        except:
            return ''

    def get_userinfo(self):
        try:
            nickNameSoup = self.soup_.find('a', class_='name')
            nick_name = nickNameSoup.get_text()
            url = nickNameSoup.attrs['href']
            pattern = '/[\d]+\?'
            u_id = re.findall(pattern, url)[0].replace('/', '').replace('?', '')
            return nick_name, url, u_id
        except:
            return '', '', ''


    def get_text(self):
        try:
            outTxt = self.soup_.find_all('p', class_='txt')
            text =  str(outTxt[0].get_text()).strip().replace('收起全文d', '')
            return text
        except:
            return ''

    def get_location(self):
        try:
            pattern = '<a href="http://t.cn/[\S\s]*?</a>'
            results = re.findall(pattern, str(self.block_))
            for result in results:
                if '<i class="wbicon">2</i>' in result:
                    soup_temp = BeautifulSoup(str(result), 'html.parser')
                    location_text = soup_temp.find('a')
                    location = location_text.get_text()
                    return location.replace('2', '')
            return ''

        except:
            return ''




    def get_time_device(self):
        try:
            pList = self.soup_.find_all('p', class_='from')[-1]
            soupTemp = BeautifulSoup(str(pList), 'html.parser')
            try:
                time = soupTemp.find_all('a')[0].get_text().replace('\n','').strip()
            except:
                time = ''
            try:
                device = soupTemp.find_all('a')[1].get_text().replace('\n','').strip()
            except:
                device = ''
            return time, device
        except:
            return '', ''


    def get_nums(self):
        try:
            liList = self.soup_.find('div', class_='card-act')
            soupTemp = BeautifulSoup(str(liList), 'html.parser')
            actList = soupTemp.find_all('li')
            transmitNum = str(actList[1].get_text()).replace('转发', '')
            commentNum = str(actList[2].get_text()).replace('评论', '')
            likeNum = str(BeautifulSoup(str(actList[3]), 'html.parser').find('em').get_text())
            if transmitNum.strip() == '':
                transmitNum = 0
            if commentNum.strip() == '':
                commentNum = 0
            if likeNum.strip() == '':
                likeNum = 0
            return int(transmitNum), int(commentNum), int(likeNum)
        except:
            return 0, 0, 0

    def get_tr_info(self):
        s = self.soup_.find('div', class_='card-comment')
        in_parser = weiboTrinParser(s)
        return in_parser.info







