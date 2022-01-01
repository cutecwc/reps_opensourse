# 第十个文件
# include <psr>
# 笔趣阁以外的网站，如二手房、二手车网站进行爬取
# 使用了MySQL数据库，目的服务器IP为：192.168.129.128，sql密码为：MXcc123..
# 参考：https://blog.csdn.net/Angelxiqi/article/details/119155252（关于安装数据库Mysql部分）
# 如何启动MYSQL：systemctl start  mysqld.service
# 查看当前数据库状态：systemctl status mysqld 
# 启动数据库：mysql -u root -p

from urllib import parse, request
import re
import time
import random
import csv

ua_list = [
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
    'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
]

class ParseUser(object):
    def __init__(self) :
        #####################################################################################################
        self.urls='https://ganzhou.anjuke.com/'
        #####################################################################################################
    
    def get_html(self,urls):
        req=request.Request(url=urls,headers={'User-Agent':random.choice(ua_list)})
        res=request.urlopen(req)
        htmls=res.read().decode('gbk','ignore')
        print(htmls)
        self.analyse(html=htmls)# 按照正则表达式解析

    def analyse(self,html):
        #####################################################################################################
        '''
        <a title=.*?><div class="img-wrap">.*?</div><dl class=".*?"><dt>(.*?)</dt><dd><span>(.*?)</span>(.*?)</dd><dd class="grey">(.*?)</dd></dl></a>

        //*[@id="content"]/div[1]/div[7]/div/ul/li[1]/a[1]
        /html/body/div[2]/div[2]/div[1]/div[7]/div/ul/li[1]/a[1]
        #content > div.left-cont.fl > div:nth-child(7) > div > ul > li:nth-child(1) > a:nth-child(2)
        document.querySelector("#content > div.left-cont.fl > div:nth-child(7) > div > ul > li:nth-child(1) > a:nth-child(2)")
        '''
        reptn='<a title=.*?>.*?<dl class=".*?"><dt>(.*?)</dt><dd><span>(.*?)</span>(.*?)</dd><dd class=".*?">(.*?)</dd></dl></a>'
        #####################################################################################################
        print('start analyse')
        ptn=re.compile(reptn,re.S)
        print('re.compile')
        lists=ptn.findall(html)
        print('ptn.findall')
        self.savefile(listv=lists)

    def savefile(self,listv):
        print('start savefiles')
        print(listv)
        #####################################################################################################
        with open('Try4/anjuke/1.csv','a',newline='',encoding='utf-8') as f:
        #####################################################################################################
            writer=csv.writer(f)
            for r in listv:
                #############################################################################################
                name=r[0].strip()
                money=r[1].strip()
                uiits=r[2].strip()
                withwhs=r[3].strip()
                lst=[name,money,uiits,withwhs]
                #############################################################################################
                writer.writerow(lst)
                print(name+'\t'+'money:'+money+uiits+'\t'+withwhs)


    def run(self):
        #####################################################################################################
        # for offset in range(0,11,10):
            # oft={
            #     'offset':str(offset),
            # }
            # ofts=parse.urlencode(oft)
            # url=self.urls.format(ofts)
        url=self.urls
        self.get_html(url)

        time.sleep(random.uniform(3,4))
        #####################################################################################################



def lines():
    print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

def main():
    try:
        pa=ParseUser()
        pa.run()
        print("done")
    except Exception as e:
        print("something error",e)

if __name__=='__main__':
    main()







