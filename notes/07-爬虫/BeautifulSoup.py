# !/usr/bin/env python
# _*_ coding:utf-8 _*_


import requests
from bs4 import BeautifulSoup


class Tencent_spider(object):
    def __init__(self):
        self.base_url = 'https://hr.tencent.com/position.php?keywords=python&tid=0&lid=2218&start=30#a'
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}

    # 发送请求
    def send_request(self, url, params={}):
        try:
            response = requests.get(url=url, params=params, headers=self.headers)
            return response.content
        except Exception, err:
            print err

    # 解析数据
    def analysis_data(self, data):

        # 1.转类型
        soup = BeautifulSoup(data, 'lxml')
        # 2.解析

    # 写入本地文件
    def write_file(self, data):
        with open('5Tencent.html', 'w') as f:
            f.write(data)

    # 调度
    def run(self):
        # 1.拼接字符 和参数
        # 2.发送请求
        # 3.解析数据
        # 4.保存本地


if __name__ == '__main__':
    tool = Tencent_spider()
    tool.run()