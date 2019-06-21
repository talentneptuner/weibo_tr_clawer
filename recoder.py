import pymysql

class Recoder():

    def __init__(self):
        self.conn_ = pymysql.connect(host='192.168.22.241', port=3306, user='my_admin', passwd='Alex19900807.',
                               db='yibin_tr',
                               charset='utf8mb4')  # 基本的本机MYSQL配置
        self.cursor_ = self.conn_.cursor()

    def save_weibo(self, data):
        try:
            sql = 'INSERT IGNORE into weibo(mid, nick_name,url, u_id, out_txt, location, img_list, time, device, transmit_num,' \
                  'comment_num, like_num, now_time, trans) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s,%s)'
            # try:
            result = self.cursor_.executemany(sql, data)
            self.conn_.commit()
            return result
        except pymysql.err.IntegrityError:
            return 0

        # except:
        #     p

    def save_url(self,url):
        sql = 'insert into error_url values (%s)'
        self.cursor_.execute(sql, url)
        self.conn_.commit()

    def save_weibo_one(self, data):
        try:
            sql = 'insert ignore into weibo(mid, nick_name, out_txt, location, img_list, time, device, transmit_num,' \
                  'comment_num, like_num, now_time) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
            # try:
            result = self.cursor_.execute(sql, data)
            self.conn_.commit()
            return result
        except pymysql.err.IntegrityError:
            return 0

    def get_error_urls(self):
        sql = 'select * from error_url'
        self.cursor_.execute(sql)
        urls = self.cursor_.fetchall()
        sql = 'delete from error_url'
        self.cursor_.execute(sql)
        self.conn_.commit()
        return [i[0] for i in urls]
