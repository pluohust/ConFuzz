#!/usr/bin/python
#-*- coding:utf-8 -*-

from sulley import *
from requests import http_get
from requests import http_header
from requests import http_post

def httpFuzz():
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
	sess.connect(s_get("HTTP VERBS"))
	sess.fuzz()
	print "Fuzzing has completed!"

httpFuzz()
