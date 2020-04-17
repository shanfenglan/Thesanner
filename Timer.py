#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created by shanfenglan on 2019-08-13

import time


class Mytimer():

    def __init__(self):
        self.last = []
        self.start1 = []
        self.stop1 = []
        self.prompt2 = []
        self.unit = ['year', 'month', 'day', 'hour', 'minute', 'second']
        self.sum = 0
        self.lastest = [0, 0, 0, 0, 0, 0]
        self.finally_sum = []
        self.demo = [0, 0, 0, 0, 0, 0]
        self.last_list = []

    # start the timer
    def start(self):
        self.start1 = time.localtime()

    # 停止计时

    def stop(self):
        self.stop1 = time.localtime()
        for index in range(6):
            self.lastest[index] += int(self.stop1[index]) - int(self.start1[index])

        print('The total time of the program running is ', end='')
        for index in range(6):
            self.last_list.append(' ' + str(self.lastest[index]) + ' ' + self.unit[index])
            if self.lastest[index] != 0:
                print(self.last_list[index]+ ' ', end='')

