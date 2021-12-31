# 第七个文件，正则匹配
import re
def abc():
    html="""
        <div><p>www.biancheng.net</p></div>
        <div><p>编程帮</p></div>
    """
    print('\n')
    #贪婪匹配，re.S可以匹配换行符
    #创建正则表达式对象
    pattern=re.compile('<div><p>.*</p></div>',re.S)
    #匹配HTMLX元素，提取信息
    re_list=pattern.findall(html)
    print(re_list)
    print('\n')
    #非贪婪模式匹配，re.S可以匹配换行符
    pattern=re.compile('<div><p>.*?</p></div>',re.S)
    re_list=pattern.findall(html)
    print(re_list)
    print('\n')

def abc1():
    html="""
        <div class="movie-item-info">
        <p class="name">
        <a title="你好，李焕英">你好，李焕英</a>
        </p>
        <p class="star">
        主演：贾玲,张小斐,沈腾
        </p>    
        </div>
        <div class="movie-item-info">
        <p class="name">
        <a title="刺杀，小说家">刺杀，小说家</a>
        </p>
        <p class="star">
        主演：雷佳音,杨幂,董子健,于和伟
        </p>    
        </div> 
    """
    # 寻找HTML规律，书写正则表达式，使用正则表达式分组提取信息
    pattern=re.compile(r'<div.*?<a title="(.*?)".*?star">(.*?)</p.*?div>',re.S)
    r_list=pattern.findall(html)
    print(r_list)
    # 整理数据格式并输出
    if  r_list:
        for r_info in  r_list:
            print("影片名称：",r_info[0])
            print("影片主演：",r_info[1].strip())
            print(20*"*")
def main():
    abc()
    print('\n')
    abc1()

if __name__=='__main__':
    main()

# 注意strip做一个字符串切割
# compile做一个正则生成且依据生成做匹配