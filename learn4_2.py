# 第八个文件，文件写入
# csv使得list相关的数据有规则的存储

import csv
def m1():
    # 操作文件对象时，需要添加newline参数逐行写入，否则会出现空行现象
    with open('test/eggs.csv', 'w', newline='') as csvfile:
        # delimiter 指定分隔符，默认为逗号，这里指定为空格
        # quotechar 表示引用符
        # writerow 单行写入，列表格式传入数据
        spamwriter = csv.writer(csvfile, delimiter=' ',quotechar='|')
        spamwriter.writerow(['www.biancheng.net'] * 5 + ['how are you'])
        spamwriter.writerow(['hello world', 'web site', 'www.biancheng.net'])

def m2():
    with open('test/aggs.csv', 'w', newline='') as f:
        writer = csv.writer(f)# 未指定格式
        # 注意传入数据的格式为列表元组格式
        writer.writerows([('hello','world'), ('I','love','you')])

def m3():
    with open('test/names.csv', 'w', newline='') as csvfile:
        #构建字段名称，也就是key
        fieldnames = ['first_name', 'last_name']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        # 写入字段名，当做表头
        writer.writeheader()
        # 多行写入
        writer.writerows([{'first_name': 'Baked', 'last_name': 'Beans'},{'first_name': 'Lovely', 'last_name': 'Spam'}])
        # 单行写入
        writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})

def m4():
    #read
    with open('test/eggs.csv', 'r', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
                print(', '.join(row))

def m5():
    #read2
    with open('test/names.csv',newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row['first_name'], row['last_name'])

def m6():
    #read3
    with open('test/aggs.csv','r',newline='') as csvfile:
        reader =csv.reader(csvfile)
        for row in reader:
            print(', '.join(row))

def main():
    m6()

if __name__=='__main__':
    main()