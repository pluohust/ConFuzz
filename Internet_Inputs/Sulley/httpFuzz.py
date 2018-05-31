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
	sess.connect(s_get("HTTP METHOD"))
	sess.connect(s_get("HTTP REQ"))
	sess.connect(s_get("HTTP HEADER ACCEPT"))
	sess.connect(s_get("HTTP HEADER ACCEPTCHARSET"))
	sess.connect(s_get("HTTP HEADER ACCEPTDATETIME"))
	sess.connect(s_get("HTTP HEADER ACCEPTENCODING"))
	sess.connect(s_get("HTTP HEADER ACCEPTLANGUAGE"))
	sess.connect(s_get("HTTP HEADER AUTHORIZATION"))
	sess.connect(s_get("HTTP HEADER CACHECONTROL"))
	sess.connect(s_get("HTTP HEADER CLOSE"))
	sess.connect(s_get("HTTP HEADER CONTENTLENGTH"))
	sess.connect(s_get("HTTP HEADER CONTENTMD5"))
	sess.connect(s_get("HTTP HEADER COOKIE"))
	sess.connect(s_get("HTTP HEADER DATE"))
	sess.connect(s_get("HTTP HEADER DNT"))
	sess.connect(s_get("HTTP HEADER EXPECT"))
	sess.connect(s_get("HTTP HEADER FROM"))
	sess.connect(s_get("HTTP HEADER HOST"))
	sess.connect(s_get("HTTP HEADER IFMATCH"))
	sess.connect(s_get("HTTP HEADER IFMODIFIEDSINCE"))
	sess.connect(s_get("HTTP HEADER IFNONEMATCH"))
	sess.connect(s_get("HTTP HEADER IFRANGE"))
	sess.connect(s_get("HTTP HEADER IFUNMODIFIEDSINCE"))
	sess.connect(s_get("HTTP HEADER KEEPALIVE"))
	sess.connect(s_get("HTTP HEADER MAXFORWARDS"))
	sess.connect(s_get("HTTP HEADER PRAGMA"))
	sess.connect(s_get("HTTP HEADER PROXYAUTHORIZATION"))
	sess.connect(s_get("HTTP HEADER RANGE"))
	sess.connect(s_get("HTTP HEADER REFERER"))
	sess.connect(s_get("HTTP HEADER TE"))
	sess.connect(s_get("HTTP HEADER UPGRADE"))
	sess.connect(s_get("HTTP HEADER USERAGENT"))
	sess.connect(s_get("HTTP HEADER VIA"))
	sess.connect(s_get("HTTP HEADER WARNING"))
	sess.connect(s_get("HTTP HEADER XATTDEVICEID"))
	sess.connect(s_get("HTTP HEADER XDONOTTRACK"))
	sess.connect(s_get("HTTP HEADER XFORWARDEDFOR"))
	sess.connect(s_get("HTTP HEADER XREQUESTEDWITH"))
	sess.connect(s_get("HTTP HEADER XWAPPROFILE"))
	sess.connect(s_get("HTTP VERBS POST"))
	sess.connect(s_get("HTTP VERBS POST ALL"))
	sess.connect(s_get("HTTP VERBS POST REQ"))
	sess.fuzz()
	print "Fuzzing has completed!"

httpFuzz()
