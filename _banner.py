#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created by shanfenglan on 2020/4/17
import random
def banner():
    key = random.randint(1, 9)
    keyy = int('3' + str(key))

    if key in range(0, 4):
        print("""
    \033[1;{0};40m

     _____ _          ____
    |_   _| |__   ___/ ___|  ___ __ _ _ __  _ __   ___ _ __
      | | | '_ \ / _ \___ \ / __/ _` | '_ \| '_ \ / _ \ '__|
      | | | | | |  __/___) | (_| (_| | | | | | | |  __/ |
      |_| |_| |_|\___|____/ \___\__,_|_| |_|_| |_|\___|_|

                    # Coded By Shanfenglan   
                    # github:https://github.com/shanfenglan
    \033[0m   """.format(keyy))

    elif key in range(6,9):
        print("""\033[1;30;40m
         ___________________________________ 
    < Wow,Lucky dog!  Welcome to use TheScannercowsay!! >\033[1;31;40m
     ----------------------------------- \033[1;32;40m
        \
         \
                                       .::!!!!!!!:.\033[1;33;40m
      .!!!!!:.                        .:!!!!!!!!!!!!\033[1;34;40m
      ~~~~!!!!!!.                 .:!!!!!!!!!UWWW$$$ \033[1;35;40m
          :$$NWX!!:           .:!!!!!!XUWW$$$$$$$$$P \033[1;34;40m
          $$$$$##WX!:      .<!!!!UW$$$$"  $$$$$$$$# \033[1;33;40m      
          $$$$$  $$$UX   :!!UW$$$$$$$$$   4$$$$$*\033[1;32;40m 
          ^$$$B  $$$$\     $$$$$$$$$$$$   d$$R" \033[1;31;40m
            \"*$bd$$$$      \'*$$$$$$$$$$$o+#\"
                 \"\"\"\"          """"""" 
                 
\033[1;32;40m%%%% Author: Shanfenglan $$$$
             %%%% github:https://github.com/shanfenglan $$$$
            

\033[0m
""")

    else:
        print("""
        \033[1;35;40m
     ____ 
< TheScanner is so efficient! >
 ---- 
          \
           \
            \          __---__
                    _-       /--______
               __--( /     \ )XXXXXXXXXXX\v.
             .-XXX(   O   O  )XXXXXXXXXXXXXXX-
            /XXX(       U     )        XXXXXXX\
          /XXXXX(              )--_  XXXXXXXXXXX\
         /XXXXX/ (      O     )   XXXXXX   \XXXXX\
         XXXXX/   /            XXXXXX   \__ \XXXXX
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
                  
    \033[1;33;40m<<<<<Created by Shanfenglan>>>>>\033[0m
                 <<<<<github:https://github.com/shanfenglan>>>>>
    """)

    print('\n\033[1;35;40m--------------------------------------------------------------------------------\033[0m')
# banner()
#3331112131231