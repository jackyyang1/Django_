# coding=utf-8
# 从 txt 文本读取ip 测试IP有效性 写入ok-ip.txt
import gevent
import urllib2
from gevent import monkey
# 打补丁，放猴子
monkey.patch_all()

def cishi_xici_ip(filename):
    # 代理访问百度，测试ip 有效性
    proxy_list = []
    with open(filename, "r") as f:
        lines = f.readlines()
        for i in range(0, len(lines)):
            proxy_list.append(lines[i])

    # 开始测试
    ok_ip = []
    ok_num = 0
    bad_num = 0
    for proxy_ip in proxy_list:
        proxy = {"http": proxy_ip}
        headers = {
            'Accept': '*/*',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
        }

        url = 'http://www.baidu.com'
        # 创建 管理器
        proxy_handler = urllib2.ProxyHandler(proxy)

        # 根据管理器创建 opener
        opener = urllib2.build_opener(proxy_handler)

        # 调用 open() 发起请求
        request = urllib2.Request(url, headers=headers)
        try:
            #                          2秒没响应就放弃
            resp = opener.open(request, timeout=3)
        except Exception as e:
            print "this free-proxy--%s is bad" % proxy_ip
            bad_num += 1
            print "xici-bad---%s" % bad_num
        else:
            code = resp.getcode()
            if code == 200:
                print "this free-proxy--%s is OKKKKKKK" % proxy_ip
                with open("xici-ok-ip.txt", "a+") as f:
                    f.write(proxy_ip)

                ok_ip.append(proxy_ip)
                ok_num += 1
                print "xici-ok--%s" % ok_num


def ceshi_kuai_ip(filename):
    # 代理访问百度，测试ip 有效性
    proxy_list = []
    with open(filename, "r") as f:
        lines = f.readlines()
        for i in range(0, len(lines)):
            proxy_list.append(lines[i])

    # 开始测试
    ok_ip = []
    ok_num = 0
    bad_num = 0
    for proxy_ip in proxy_list:
        proxy = {"http": proxy_ip}
        headers = {
            'Accept': '*/*',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
        }

        url = 'http://www.baidu.com'
        # 创建 管理器
        proxy_handler = urllib2.ProxyHandler(proxy)

        # 根据管理器创建 opener
        opener = urllib2.build_opener(proxy_handler)

        # 调用 open() 发起请求
        request = urllib2.Request(url, headers=headers)
        try:
            #                          3秒没响应就放弃
            resp = opener.open(request, timeout=3)
        except Exception as e:
            print "this free-proxy--%s is bad" % proxy_ip
            bad_num += 1
            print "kuai-bad---%s" % bad_num
        else:
            code = resp.getcode()
            if code == 200:
                print "this free-proxy--%s is OKKKKKKK" % proxy_ip
                with open("kuai-ok-ip.txt", "a+") as f:
                    f.write(proxy_ip)

                ok_ip.append(proxy_ip)
                ok_num += 1
                print "kuai-ok--%s" % ok_num
    print "kuai-ok--%s" % ok_num
    print "kuai-bad--%s" % bad_num

gevent.joinall([
    # 创建协程对象
    gevent.spawn(cishi_xici_ip, "xici-ip.txt"),
    gevent.spawn(ceshi_kuai_ip, "kuai-ip.txt"),
])
# if __name__ == '__main__':
    # # 要测试哪个文件就运行哪个函数
    # # cishi_xici_ip("xici-ip.txt")
    # # ceshi_kuai_ip("kuai-ip.txt")
    # pass
