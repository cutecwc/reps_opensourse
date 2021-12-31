# 第九个文件
# try to parse 
# //*[@id="app"]/div/div/div[1]/dl/dd[1]/a/img[2]
# //*[@id="app"]/div/div/div[1]/dl/dd[1]/a

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
        self.urls='https://www.xbiquge.so/'
    
    def get_html(self,urls):
        req=request.Request(url=urls,headers={'User-Agent':random.choice(ua_list)})
        res=request.urlopen(req)
        htmls=res.read().decode('gbk','ignore')
        self.analyse(html=htmls)# 按照正则表达式解析

    def analyse(self,html):
        '''
        <a href=".*?" title="(.*?)" class="image-link" data-act="boarditem-click" data-val="{(.*?)}">
        <dt><span>作者：我吃西红柿</span><a href="https://www.xbiquge.so/book/54523/" title="宇宙职业选手">宇宙职业选手</a></dt>
        '''
        reptn='<dt><span>(.*?)</span><a href=".*?" title=".*?">(.*?)</a></dt>'
        ptn=re.compile(reptn,re.S)
        lists=ptn.findall(html)
        self.savefile(listv=lists)

    def savefile(self,listv):
        with open('Try3/test1/biquge.csv','a',newline='',encoding='utf-8') as f:
            writer=csv.writer(f)
            for r in listv:
                name=r[0].strip()
                books=r[1].strip()
                lst=[name,books]
                writer.writerow(lst)
                print(name+'\t'+'bookname:'+books)


    def run(self):
        for offset in range(0,11,10):
            # oft={
            #     'offset':str(offset),
            # }
            # ofts=parse.urlencode(oft)
            # url=self.urls.format(ofts)
            url=self.urls
            self.get_html(url)

            time.sleep(random.uniform(3,4))



def lines():
    print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

def main():
    try:
        pa=ParseUser()
        pa.run()
    except Exception as e:
        print("something error",e)

if __name__=='__main__':
    main()