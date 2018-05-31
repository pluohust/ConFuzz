#!/usr/bin/python
#-*- coding:utf-8 -*-

from sulley import *
from requests import http_get
from requests import http_header
from requests import http_post

import os
import time

def httpFuzz(eachinput):
    sess=sessions.session(session_filename="./audits/http.session",sleep_time=0.0001,fuzz_mode="auto",record=True,case_filename="./audits/record.log")
    target=sessions.target("10.0.2.15",80)
    target.netmon=pedrpc.client("10.0.2.15",26001)
    target.procmon=pedrpc.client("10.0.2.15",26002)
    target.procmon_options={
        "proc_name":"httpd",
        "start_commands":['service httpd start'],
        "stop_commands":['service httpd stop']
    }
    sess.add_target(target)
    sess.connect(s_get(eachinput))
    sess.fuzz()
    print "Fuzzing has completed!"

TotalCount=0
Readhandle=open('./1', 'r')
Writehandle=open('./results', 'w')
while True:
    eachline=Readhandle.readline()
    if eachline:
        eachline=eachline.strip()
        if eachline:
            if os.path.isfile('./audits/record.log'):
                os.remove('./audits/record.log')
            if os.path.isfile('./audits/http.session'):
                os.remove('./audits/http.session')
            httpFuzz(eachline)
            Writehandle.write(eachline+': ')
            if os.path.isfile('./audits/record.log'):
                with open('./audits/record.log') as tf:
                    temp_num=sum(1 for x in tf)
                    SumOfCases=(temp_num-1)/2
                    TotalCount=TotalCount+SumOfCases
                    Writehandle.write(str(SumOfCases)+'\n')
            time.sleep(1)
    else:
        break
Readhandle.close()
Writehandle.write("\nAll Count: "+str(TotalCount)+'\n')
Writehandle.close()
