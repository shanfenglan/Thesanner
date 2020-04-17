#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created by shanfenglan on 2019-08-18

from socket import *
from optparse import OptionParser
from threading import *
import Timer
import file_operation
screenlock = Semaphore(value=1)  # append a semaphore in order to control output on the screen.

service = []
pport = []

def portScan(hostt, portt):
    global connSocket
    try:
        pport.append(str(portt))
        connSocket = socket(AF_INET, SOCK_STREAM)  # ipv4,tcp
        connSocket.connect((hostt, portt))  # concatenate target host and port

        connSocket.settimeout(30)

        demo = 'asdf'   # random string
        demo = str.encode(demo)  # transform the string to byte
        connSocket.send(demo)   # send the message in order to get the specify port's banner
        results = connSocket.recv(100)  # receive the return information
        screenlock.acquire()
        print('[+] {0} tcp open'.format(portt))
        print('[+] The banner is {0}'.format(results.decode('utf-8')))
        service.append(str(results.decode('utf-8')))
    except:
        screenlock.acquire()
        print('[+] {0} timeout'.format(portt))
        service.append('timeout')
        # raise   # get out the exception if it exist
    finally:
        screenlock.release()
        # connSocket.close()

def connScan(hostt, portt):
    a = []
    try:
        ip = gethostbyname(hostt)   # get ip by hostname
        print('[+] IP is  :{0}'.format(ip))
    except:
        print('[-] Can\'t resolve {0} :unknown host'.format(hostt))
        return
    try:
        name = gethostbyaddr(ip)  # return Host Name,alias list, ip address,the type of 'name' is list
        print('[+] Scan results for :{0}'.format(name[0]))
    except:
        print('[+] Scan results for :{0}'.format(ip))
    for tgtport in portt:
        print('[+] Scanning port {0}'.format(tgtport))
        t = Thread(target=portScan, args=(hostt, int(tgtport)))  # import the thread  in order to improve program's executable's efficiency
        t.start()
        a.append(t)
    for i in a:
        i.join()

def run(host,port):

    connScan(host, port)
    file_operation.file_operate(host,pport,service,'service')

# host = 'www.baidu.com'
# port = ['80','443']
# print(port)
# run(host,port)
# run('39.156.66.14',['80','443'])