# 第四个文件，Have a Try！
from urllib import request
from urllib import parse

def try1():
    url1='https://www.baidu.com/s?wd={}'
    word=input("输入一个关键字:")
    str1=parse.quote(word)
    endurl1=url1.format(str1)
    # 重构UA
    ua_is={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0'}
    # 给出请求
    req=request.Request(url=endurl1,headers=ua_is)
    # 获取响应
    reps=request.urlopen(req)
    # decode响应码
    anshtml1=reps.read().decode('utf-8')

    '''保存文件为html'''
    with open('test/test1.html','w',encoding='utf-8') as f:
        f.write(anshtml1)
    # 至此，我们已经可以抓取网页，并将它保存在本地了


def lines():
    print('----------------------------------------------------------------------------------------')

def main():
    lines()
    try1()
    lines()

if __name__=='__main__':
    main()  