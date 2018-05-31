#!/usr/bin/python
# -*- coding: UTF-8 -*-   

import os
import time

START='/ur/bin/python /home/luopeng/Apache/detector/detector.py -i /home/luopeng/Apache/detector/inputs'
PROCESS='/home/luopeng/Apache/detector/inputs'

while True:
    is_server='ps -ef | grep '+PROCESS+' | grep -v grep'
    server_process=(os.popen(is_server)).readlines()
    if len(server_process)>0:
        time.sleep(300)
    else:
        httpd='ps -ef | grep httpd | grep -v grep'
        get_process=(os.popen(httpd)).readlines()
        if len(get_process)>1:
            all_processes=''
            for i in range(0, len(get_process)):
                one_process=get_process[i]
                one_process=''.join(one_process)
                one_split=one_process.split()
                if len(one_split)>1 and (one_split[1]).isdigit():
                    all_processes=all_processes+' '+one_split[1]
            try:
                os.system('/usr/bin/kill -9 '+all_processes)
            time.sleep(1)
        time.sleep(0.1)
        start=os.system(START)
        time.sleep(10)
