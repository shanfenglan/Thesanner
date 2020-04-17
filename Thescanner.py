#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created by shanfenglan on 2020/2/8

import argparse,subdomain,sys,os,re,dir_scan,portscan,Timer,bruteforce,service_scan,random,_banner

def banner():
    key = random.randint(1, 9)
    keyy = int('3'+str(key))

    if key in range(0,7):
        print("""
    \033[1;{0};40m
    
     _____ _          ____
    |_   _| |__   ___/ ___|  ___ __ _ _ __  _ __   ___ _ __
      | | | '_ \ / _ \___ \ / __/ _` | '_ \| '_ \ / _ \ '__|
      | | | | | |  __/___) | (_| (_| | | | | | | |  __/ |
      |_| |_| |_|\___|____/ \___\__,_|_| |_|_| |_|\___|_|
    
                    # Coded By Shanfenglan
    \033[0m   """.format(keyy))
    else:
        print("""
         ___________________________________ 
    < Wow,Lucky dog!  Welcome to use TheScannercowsay!! >
     ----------------------------------- 
        \
         \
                                       .::!!!!!!!:.
      .!!!!!:.                        .:!!!!!!!!!!!!
      ~~~~!!!!!!.                 .:!!!!!!!!!UWWW$$$ 
          :$$NWX!!:           .:!!!!!!XUWW$$$$$$$$$P 
          $$$$$##WX!:      .<!!!!UW$$$$"  $$$$$$$$#       \033[1;32;40m<<<<<Coded By Shanfenglan>>>>>\033[0m
          $$$$$  $$$UX   :!!UW$$$$$$$$$   4$$$$$* 
          ^$$$B  $$$$\     $$$$$$$$$$$$   d$$R" 
            \"*$bd$$$$      \'*$$$$$$$$$$$o+#\" 
                 \"\"\"\"          """"""" 
                    
        """)
    
    print('\n\033[1;35;40m--------------------------------------------------------------------------------\033[0m')


def parser_error(errmsg):
    print("Usage: python3 " + sys.argv[0] + " [Options] use -h for help. \n")
    errormessage = "Error: " + errmsg
    print("\033[1;36;40m"+errormessage+"\033[0m")
    sys.exit()


def parse_args():
    _banner.banner()
    # parse the arguments
    parser = argparse.ArgumentParser(epilog='\tExample: \r\npython ' + sys.argv[0] + " -d google.com")
    parser.error = parser_error  # rewrite function
    parser._optionals.title = "OPTIONS"
    parser.add_argument('-d', '--domain', help="Domain name to enumerate it's subdomains,exp:Thescanner.py -d www.qq.com",default=None)
    parser.add_argument('-b', '--bruteforce', help='Enable the  bruteforce module,exp: Thescanner.py -b baidu.com', default=False)
    parser.add_argument('-p', '--ports', help='Automated port scanning,exp:Thescanner.py -ip 120.79.88.157 -p 80 443 22', nargs='*', default=None)
    parser.add_argument('-s', '--service', help='Automated service scanning,exp:Thescanner.py -ip 39.156.66.14 -s 80 ', nargs='*', default=None)
    parser.add_argument('-dir', '--directory', help='Automated directory scanning,exp:Thescanner.py -dir http://www.qq.com -t 100', nargs='?', default=False)
    parser.add_argument('-dict', '--dictionary', help='Dictionary path', nargs='?', default=None)
    parser.add_argument('-ip', help='ip address,Separated by space,exp:Thescanner.py -ip 39.156.66.14 -s 80 ',nargs='*')
    parser.add_argument('-t', '--threads', help='Number of threads to use for the specific feature named directory scan or brute', type=int, default=30)
    return parser.parse_args()


def sub_scan(domain):
    print("subdomainscan is running......\n")
    subdomain.subdomain_scan(domain)


def port(ip, portt):
    print("port scanning is running......\n")
    portscan.port_s(ip=ip, port=portt)

def brute(domain,dict,thread):
    print('The brute scanning for subdomain is running.....\n')
    if dict is None:
        position = os.getcwd()
        position = position + '/_dict/222.txt'
        # print(position)
    else:
        position = dict
    bruteforce.bruteforce(domain,position,thread)

def service_sc(ip,service_port):
    print('service scanning is running....\n')
    ip = ip[0]
    service_scan.run(ip,service_port)
def dir(url, dict, thread):
    print('Directory scanning is running....\n')
    if dict is None:
        position = os.getcwd()
        position = position + '/_dict/345.txt'
        # print(position)
    else:
        position = dict

    execute = dir_scan.dir_scanner(url, position, thread)
    execute.run()
    execute.output()


def main():
    value = parse_args()
    dictionary = value.dictionary
    domain = value.domain
    service_port = value.service
    ip = value.ip
    brutee = value.bruteforce
    port1 = value.ports
    is_directory = value.directory
    thread = value.threads
    if domain is None and ip is None and is_directory is False and brutee is False:
        print('\033[1;36;40m\n[-]Error!!! You must have \'-d\' or \'-ip\' or \'-dir\' or \'-b \' in your parameter.\n\033[0m')
        sys.exit()

    if brutee is False:
        pass                      #NOT Brute ，Identify other options
    else:
        brute(brutee,dictionary,thread)
    if port1 is None:
        pass                        #NOT port scan，Identify other options
    else:
        print('The scanned port : ' + str(port1[:]).strip('[]'))
        port(ip=ip, portt=port1)
    if service_port is None:
        pass
    else:
        print('The scanned port : ' + str(service_port[:]).strip('[]'))
        service_sc(ip, service_port)
    if is_directory is False:
        pass                         #NOT directory scan，prepare to perform a subdomain scan
    else:
        dir(is_directory, dictionary, thread)
    if domain is not None:
        sub_scan(domain)


if __name__ == '__main__':
    time = Timer.Mytimer()
    time.start()

    main()
    print('\n\033[1;36;40m--------------------------------------------------------------------------------\033[0m')
    time.stop()
    print('\n\n[-]The scanning is over.\n')