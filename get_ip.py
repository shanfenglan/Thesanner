#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created by shanfenglan on 2020/4/3
from socket import *



def getip(sitee):
    ip = []
    for site in sitee:
        a=gethostbyname(site)
        ip.append(a)
    return ip
