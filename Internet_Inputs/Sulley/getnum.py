#!/usr/bin/python
#-*- coding:utf-8 -*-

import os


if os.path.isfile('./audits/record.log'):
    with open('./audits/record.log') as tf:
        temp_num=sum(1 for x in tf)
        SumOfCases=(temp_num-1)/2
        print str(SumOfCases)
