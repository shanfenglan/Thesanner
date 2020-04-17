# -*- coding:UTF-8 -*-
import argparse
import re
import sys
import time
import requests,file_operation,get_ip,threading

sites = []

def subdomain_scan(domainn):
    domain = domainn
    head = \
        {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:72.0) Gecko/20100101 Firefox/72.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
        'Accept-Encoding': 'gzip, deflate, br'
        }


    lock = threading.Lock()
    pattern = 'class="c-showurl" style="text-decoration:none;">(.*?)/&nbsp;</a>'
    page_judge = '<span class="pc">(.*?)<'

    demo = 0
    k = 0
    kk = str(k)
    url = "https://www.baidu.com/s?wd=site%3A{1}&pn={0}&oq=site%3A{2}&tn=monline_4_dg&ie=utf-8".format(kk, domain,
                                                                                                       domain)
    response = requests.get(url, headers=head).text
    time.sleep(3)
    subdomains = re.findall(page_judge, response)
    # print(subdomains)
    for i in subdomains:
        if int(i) > int(demo):
            demo = i
    page_num = demo


    # print(page_num)




    def multiple_t(url):
        global sites
        response = requests.get(url, headers=head).text
        # print(response)
        # time.sleep(3)
        subdomains = re.findall(pattern, response)
        lock.acquire()
        sites += (list(subdomains))
        # print(sites)
        lock.release()

    sum_thread=[]

    for i in range(int(page_num)):
        k = i * 10
        kk = str(k)
        url = "https://www.baidu.com/s?wd=site%3A{1}&pn={0}&oq=site%3A{2}&tn=monline_4_dg&ie=utf-8".format(kk, domain,
                                                                                                           domain)
        # time.sleep(3)
        # print(url)
        t = threading.Thread(target=multiple_t, args=(url,))
        t.start()
        sum_thread.append(t)

    for i in sum_thread:
        i.join(10)

    global sites
    siteee = list(set(sites))
    final_site=[]
    for i in siteee:
        plain = re.sub(r'http://|https://', '', i)
        plain = re.sub(r'com.*', 'com', plain)
        final_site.append(plain)
    print("The subdomain are ：" + str(final_site))
    ip = get_ip.getip(final_site)
    file_operation.file_operate(domain,final_site,ip,'domain')






# subdomain_scan('qq.com')
