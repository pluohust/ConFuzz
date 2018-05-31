#!/usr/bin/python
# -*- coding: UTF-8 -*-   

import os
import time

small_ps=''

while True:
    nginx='ps -ef | grep nginx | grep -v grep'
    get_process=(os.popen(nginx)).readlines()
    all_processes=''
    small_process=''
    if len(get_process)>1:
        for i in range(0, len(get_process)):
            this_process=get_process[i]
            this_process=''.join(this_process)
            this_split=this_process.split()
            if len(this_split)>1 and (this_split[1]).isdigit():
                all_processes=all_processes+' '+this_split[1]
                if i==0:
                    small_process=this_split[1]
                elif small_process > this_split[1]:
                    small_process=this_split[1]
        print all_processes
        if small_ps.strip() == small_process.strip():
            try:
                os.system('/usr/bin/kill -9 '+all_processes)
                print 'kill one'
            except Exception, e:
                print e
        small_ps = small_process
    time.sleep(500)