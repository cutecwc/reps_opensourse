# 第五个文件，Have a Try！
from urllib import request
from urllib import parse
import random
import time
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
class Psr(object):
    def __init__(self):
        self.urls='https://www.baidu.com/s?{}'

    def get_html(self,urls):
        req=request.Request(url=urls,headers={'User-Agent':random.choice(ua_list)})
        res=request.urlopen(req)
        htmls=res.read().decode('gbk','ignore')
        return htmls

    def analyse(self):
        pass

    def savefile(self,filename,html):
        filetip='test/'+filename+'.html'
        #file location and name in filename
        with open(filetip,'w') as f:
            f.write(html)

    def run(self):
        kys=input("输入一个关键字去查询：")#string, some kys to search
        nob1=int(input("输入起始页（推荐为1）"))#number
        nob2=int(input("输入一个终止页（推荐小于十）"))#number
        for page in range(nob1,nob2+1):
            pn=(page-1)*10
            kystimes={
                'wd':kys,
                'pn':str(pn),
            }
            kystimes=parse.urlencode(kystimes)
            urls=self.urls.format(kystimes)

            htmllist=self.get_html(urls)
            filenames='搜索结果：{}--第{}页'.format(kys,page)
            self.savefile(filename=filenames,html=htmllist)
            print("第{}页保存成功".format(page))
            time.sleep(random.randint(2,3))#单位是秒


def lines():
    print('----------------------------------------------------------------------------------------')

def main():
    lines()
    start=time.time()#计时程序
    testcls=Psr()
    testcls.run()
    end=time.time()

    print('执行了：%.2f'%(end-start))
    lines()

if __name__=='__main__':
    main()  

#总体面向对象的爬虫结构如上
#多爬了百度几次就全是安全验证的网页了，也许会有其他解决方法。。。