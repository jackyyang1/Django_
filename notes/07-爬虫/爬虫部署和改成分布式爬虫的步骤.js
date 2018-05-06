*******************************************************
一.scrapyd进行项目远程部署和监控
    
    1.安装:
        服务端;pip install scrapyd
        客户端: pip install scrapyd-client
        
    2.启动服务:
        sudo scrapyd    

    3.部署文件  scrapy.cfg
        ----------------------------
        [deploy:scrapyd_Tencent]
        url = http://localhost:6800/
        project = Tencent
        ----------------------------

    4.部署爬虫的项目到 服务
        4.1 cd到项目
        4.2客户端 :scrapyd-deploy scrapyd_Tencent -p Tencent


    5.开启爬虫
        curl http://localhost:6800/schedule.json -d project=Tencent -d spider=tencent3
        
        查看日志log

    6.关闭爬虫 (jonid 要看开启的时候返回的那个)
        curl http://localhost:6800/cancel.json -d project=Tencent -d job=3ec1111e0a2311e89c5dacbc329a1151



    注:1.把爬虫运行在服务端,只需输入ip就可 查看爬虫进度,和网络日志
            只要开启了服务器:scrapyd  就可以访问localhost:6800

        2.部署的时候记得要开启延时 :DOWNLOAD_DELAY = 3
        3.第四部启动scrapyd客户端 时 ,正确会显示如下;
            Packing version 1519543006
            Deploying to project "Tencent" in http://localhost:6800/addversion.json
            Server response (200):
            {"version": "1519543006", "project": "Tencent", "spiders": 1, "node_name": "\u201c
            \u674e\u76f8\u8d6b\u201d", "status": "ok"}
            注: node_name 是系统自己起的别名 

        4.在windows下运行部署需要安装调度方法 :curl
             下载并配置环境变量

        5.开启爬虫任务:注:还是在Ubuntu上面开启爬虫比较好,因为在windows上
            会报错 : 'builtins.NotImplementedError: spawnProcess not available since pywin32 is not installed.
            即使安装了 pip3 install pywin32 还是会报错
            可以登陆 localhost:6800 但是 点击 Jobs 无法查看到进行的任务!
            但相同的代码在 Ubuntu上就能完美运行! 可以点击 log 查看日志!
            如果想中断爬虫: 就输入 关闭爬虫的命令

        6.重点: 如果不手动关闭爬虫,就算信息爬取完毕,爬虫仍然是出于启动状态!
                正常情况下 关闭爬虫过一阵子才会关闭!


********************************************************
二.分布式爬虫:

1. spider
    1.from scrapy_redis.spiders import RedisSpider
    2.修改继承关系
    3.redis_key = 'api:start_urls'
    4. allow_domains 域名范围

2. setting

    # 1.设置 分布式的 去重组件
    DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
    # 2.设置 分布式的 调度器
    SCHEDULER = "scrapy_redis.scheduler.Scheduler"

    # 3.允许爬虫中途停止 中断
    SCHEDULER_PERSIST = True

    # 4.设置 redis 数据库的端口号 和IP
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379

    # 5.设置 redis的下载管道
    'scrapy_redis.pipelines.RedisPipeline': 400
    
    # 6.开启爬虫:
    scrapy crawl myspider

    7.在redis客户端输入下列命令告知爬虫,让它干活!
    redis 127.0.0.1:6379> lpush myspider:start_urls "http://www.dmoztools.net/" 