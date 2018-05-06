# -*- coding:utf8 -*-
# 爬取西刺--存到 txt
# 爬快代理存到txt

import urllib2
import re
import time
import ssl
import ceshi_ip


def xici_download():
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        'Hosts': 'hm.baidu.com',
        'Referer': 'http://www.xicidaili.com/nn',
        'Connection': 'keep-alive'
    }

    # 指定爬取范围（这里是第1~10页）
    for i in range(1, 15):

        url = 'http://www.xicidaili.com/nn/' + str(i)
        req = urllib2.Request(url=url, headers=headers)
        res = urllib2.urlopen(req).read()

        # 提取ip和端口
        # 如果不使用re.S参数，则只在每一行内进行匹配，如果一行没有，就换下一行重新开始，不会跨行。
        # 而使用re.S参数以后，正则表达式会将这个字符串作为一个整体，
        # 将“\n”当做一个普通的字符加入到这个字符串中，在整体中进行匹配。
        ip_list = re.findall("(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*?(\d{2,6})", res, re.S)

        # 将提取的ip和端口写入文件
        with open("xici-ip.txt", "a+") as f:
            for li in ip_list:
                ip = li[0] + ':' + li[1] + '\n'
                f.write(ip)
        print "xici %s page save ok" % i
        time.sleep(5)


def kuai_download():
    # 快代理
    # 指定爬取范围（这里是第1~10页）
    for i in range(1, 15):
        url = 'https://www.kuaidaili.com/free/inha/' + str(i) + '/'
        headers = {
            'Accept': '*/*',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
            'Hosts': 'hm.baidu.com',
            'Referer': url,
            'Connection': 'keep-alive'
        }

        # https 网站需要证书，忽略
        request = urllib2.Request(url, headers=headers)
        context = ssl._create_unverified_context()
        response = urllib2.urlopen(request, context=context)
        res = response.read()
        # 提取ip和端口
        # 如果不使用re.S参数，则只在每一行内进行匹配，如果一行没有，就换下一行重新开始，不会跨行。
        # 而使用re.S参数以后，正则表达式会将这个字符串作为一个整体，
        # 将“\n”当做一个普通的字符加入到这个字符串中，在整体中进行匹配。
        ip_list = re.findall("(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*?(\d{2,6})", res, re.S)

        # 将提取的ip和端口写入文件
        with open("kuai-ip.txt", "a+") as f:
            for li in ip_list:
                ip = li[0] + ':' + li[1] + '\n'
                f.write(ip)
        print "kuai %s page save ok" % i
        time.sleep(5)


if __name__ == '__main__':
    # 西刺的地址 'http://www.xicidaili.com/nn/xxx'
    # 快代理地址 'https://www.kuaidaili.com/free/inha/xxx/

    # 快代理 IP 下载  --默认下载1-10页
    kuai_download()
    # 西刺下载
    xici_download()

    # 测试 有效的 ip

    # ceshi_ip.ceshi_kuai_ip("kuai-ip.txt")
    # ceshi_ip.cishi_xici_ip("xici-ip.txt")
