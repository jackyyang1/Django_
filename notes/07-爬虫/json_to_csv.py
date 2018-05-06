# coding=utf-8

import json
import csv
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8') # 解决ascii报错

def json_to_csv():

    # 1.读取json文件的数据
    json_file = open('05.tencent4.json','r')
    # 2.csv的写入文件对象
    csv_file = open('06tencent.csv','w')

    # 3.取出数据 :1.表头,2.内容
    json_list = json.load(json_file)  # 把文件转成python对象用load(
    # 3.1 取表头 -->最上面的 头
    sheet_title = json_list[0].keys()
    # 3,2 取所有内容
    json_values = []
    for dict in json_list:
        json_values.append(dict.values())

    # 4.写入csv文件
    # 4.1根据文件对象.生成读写器
    csv_writer = csv.writer(csv_file)

    # 4.2写入表头
    csv_writer.writerow(sheet_title)
    # 4.3 写入内容
    csv_writer.writerows(json_values)

    # 5.关闭文件
    csv_file.close()
    json_file.close()

    print('保存结束')


if __name__ == '__main__':
    json_to_csv()
