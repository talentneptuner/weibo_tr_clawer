import pymysql
import urllib
import time

if __name__ == '__main__':
    conn = pymysql.connect(host='192.168.22.241', port=3306, user='my_admin', passwd='Alex19900807.',
                               db='yibin_earthquake',
                               charset='utf8mb4')  # 基本的本机MYSQL配置
    sql = 'select id,mid,img_list from weibo where img_list != ""'
    cursor_s = conn.cursor()
    cursor_s.execute(sql)
    data = cursor_s.fetchall()

    all_img = []
    save_sus = []

    for item in data:
        img_list = set(item[2].split('|'))
        for index,img in enumerate(img_list):
            all_img.append(dict(id=item[0], name=str(item[1])+'-'+str(index), img_url=img, mid=item[1]))

    print(len(all_img))

    for item in all_img:
        print(item)
        if item['img_url'].startswith("http://") or item['img_url'].startswith("https://"):
            src = item['img_url']
        else:
            src = 'https://{}'.format(item['img_url'].lstrip('//'))
        try:
            src = src.replace('thumb150', 'mw690')
            img_local = r'C:\D\Files\data\weiboImageh\{}.jpg'.format(item['name'])
            urllib.request.urlretrieve(src, img_local)
            sql = 'replace into image VALUES (%s, %s) '
            cursor_s.execute(sql,(item['mid'],item['name']))
            conn.commit()
        except:
            try:
                time.sleep(2)
                img_local = r'C:\D\Files\data\weiboImageh\{}.jpg'.format(item['name'])
                urllib.request.urlretrieve(src, img_local)
                sql = 'replace into weibo_img VALUES (%s, %s) '
                cursor_s.execute(sql, (item['mid'], item['name']))
                conn.commit()
            except:
                print(item['img_url'])
                print(src)
                print('下载失败')