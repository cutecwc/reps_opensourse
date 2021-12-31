# 第六个文件，正则表达式
#!/usr/bin/python
# -* coding: UTF-8 -*-
# 第六个文件
# include re
# 正则表达式
import re
text = 'the man whose name is written in this note shall die'

def test1():
    print(re.match('www','www.baidu.com').span())
    print(re.match('com','www.baidu.com'))

# 火红的萨日朗
def test2():
    print(re.match('the',text).group())#从开头匹配the，非完全匹配
    print(re.findall('die$',text)[0])

def test3():
    # 正则表达式dot
    patten='n.me'
    print(re.match(patten,text))#match 只能匹配开头的字符 有点拉
    print(type(re.findall(patten,text)))#这是一个list，故不能直接输出
    print(re.findall(patten,text)[0])

def test4():
    # 正则表达式\
    txt1 = 'this+is+a*test'
    ptn1 = 'is\+'
    print(re.findall(ptn1,txt1))

def test5():
    # 正则表达式?
    # 问号表示匹配前面的字符0或者1次
    txt3 = 'abcmnabcdpqabqabcdd'
    ptn3 = 'abcd?'
    print(re.findall(ptn3,txt3)) # ['abc', 'abcd', 'abcd']
    # 此外，问号还可以表示非贪婪搜索，即在数量不指定的时候，贪婪返回最长的，而非贪婪返回最少的
    ptn3greedy = 'abcd*'
    ptn3nogreedy = 'abcd*?'
    print(re.findall(ptn3greedy,txt3)) # ['abc', 'abcd', 'abcdd'] 优先匹配两个d的（d最多的）
    print(re.findall(ptn3nogreedy,txt3)) # ['abc', 'abcd', 'abc'] 优先匹配0个d的（d最少的）

def test6():
    # 正则表达式^ and $ and . and |
    # ^ 和 $ ：hat符号表示匹配每行的开头，dollar符号表示匹配每行的结尾
    txt4 = 'machine learning is fun \ndeep learning is not\nbut'
    print(txt4)
    ptn41 = '^mac'
    ptn42 = '.t'
    print(re.findall(ptn41,txt4))# ['mac']
    print(re.findall(ptn42,txt4)) # ['ot', 'ut']
    ptn43='ee|ea'
    print(re.findall(ptn43,txt4))

def test7():
    # 正则表达式()
    txt6 = 'stop!stoop!stooop!stoooop!!!'
    ptn61 = 'sto{2,3}p'
    ptn62 = 'sto{1}p'
    ptn63 = 'sto{2,}p'
    print( re.findall(ptn61,txt6)) # ['stoop', 'stooop']
    print( re.findall(ptn62,txt6)) # ['stop']
    print( re.findall(ptn63,txt6)) # ['stoop', 'stooop', 'stoooop']

def test8():
    # 老人地铁手机?
    # regex.findal(string,pos,endpos)
    # re.split(pattern,string,flag=0)
    # text = 'the man whose name is written in this note shall die'
    pass

def main():
    print('.................................................')
    test6()
if __name__=='__main__':
    main()