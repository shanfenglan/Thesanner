# Thesanner
An simple scanner that contains feature are portscan,subdomain scan,service scan,etc

It is my first complete program,if you have advices and questions,please tell me . 

thank you so much.

# Usage:
   
```
  python3 Thescanner.py -h  

        
     ____ 
< TheScanner is so efficient! >
 ---- 
                                 \          __---__
                    _-       /--______
               __--( /     \ )XXXXXXXXXXX
                                         .
             .-XXX(   O   O  )XXXXXXXXXXXXXXX-
            /XXX(       U     )        XXXXXXX          /XXXXX(              )--_  XXXXXXXXXXX         /XXXXX/ (      O     )   XXXXXX   \XXXXX         XXXXX/   /            XXXXXX   \__ \XXXXX
         XXXXXX__/          XXXXXX         \__---->
 ---___  XXX__/          XXXXXX      \__         /
   \-  --__/   ___/\  XXXXXX            /  ___--/=
    \-\    ___/    XXXXXX              '--- XXXXXX          
       \-\/XXX\ XXXXXX                      /XXXXX
         \XXXXXXXXX   \                    /XXXXX/
          \XXXXXX      >                 _/XXXXX/
            \XXXXX--__/              __-- XXXX/
             -XXXXXXXX---------------  XXXXXX-
                \XXXXXXXXXXXXXXXXXXXXXXXXXX/
                  ""VXXXXXXXXXXXXXXXXXXV""
                  
    <<<<<Created by Shanfenglan>>>>>
                 <<<<<github:https://github.com/shanfenglan>>>>>
    

--------------------------------------------------------------------------------
usage: Thescanner.py [-h] [-d DOMAIN] [-b BRUTEFORCE] [-p [PORTS [PORTS ...]]]
                     [-s [SERVICE [SERVICE ...]]] [-dir [DIRECTORY]]
                     [-dict [DICTIONARY]] [-ip [IP [IP ...]]] [-t THREADS]

OPTIONS:
  -h, --help            show this help message and exit
  -d DOMAIN, --domain DOMAIN
                        Domain name to enumerate it's
                        subdomains,exp:Thescanner.py -d www.qq.com
  -b BRUTEFORCE, --bruteforce BRUTEFORCE
                        Enable the bruteforce module,exp: Thescanner.py -b
                        baidu.com
  -p [PORTS [PORTS ...]], --ports [PORTS [PORTS ...]]
                        Automated port scanning,exp:Thescanner.py -ip
                        120.79.88.157 -p 80 443 22
  -s [SERVICE [SERVICE ...]], --service [SERVICE [SERVICE ...]]
                        Automated service scanning,exp:Thescanner.py -ip
                        39.156.66.14 -s 80
  -dir [DIRECTORY], --directory [DIRECTORY]
                        Automated directory scanning,exp:Thescanner.py -dir
                        http://www.qq.com -t 100
  -dict [DICTIONARY], --dictionary [DICTIONARY]
                        Dictionary path
  -ip [IP [IP ...]]     ip address,Separated by space,exp:Thescanner.py -ip
                        39.156.66.14 -s 80
  -t THREADS, --threads THREADS
                        Number of threads to use for the specific feature
                        named directory scan or brute

Example: python Thescanner.py -d google.com

```
