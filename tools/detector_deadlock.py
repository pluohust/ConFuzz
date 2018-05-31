#!/usr/bin/python 
# -*- coding: UTF-8 -*-   

import os
import sys
import getopt
import time
import subprocess
import shutil
import threading

START=''
INDIR=''
NAME=''
KILL=''

all_inputs=[]
end_flag=0

def GetArgsFromFile(arg_file):
	global START, INDIR, NAME, KILL
	
	readhandle=open(arg_file, 'r')
	while True:
		getoneline=readhandle.readline()
		if getoneline:
			if 'start: ' in getoneline:
				START=((getoneline.split('start: '))[1]).strip()
			elif 'indir: ' in getoneline:
				INDIR=((getoneline.split('indir: '))[1]).strip()
			elif 'name: ' in getoneline:
				NAME=((getoneline.split('name: '))[1]).strip()
			elif 'kill: ' in getoneline:
				KILL=((getoneline.split('kill: '))[1]).strip()
		else:
			break
	readhandle.close()
	if len(START)<1 or len(INDIR)<1 or len(NAME)<1 or len(KILL)<1:
		print('the args are not enough in'+arg_file+'!')
		sys.exit()

def Usage():
	print('-h help information')
	print('-i the argvs from file, and the format is that:')
	print('---> start: the cmd line of server, such as \"pin -t *.so -- httpd\"')
	print('---> indir: the inputs dir')
	print('---> dir: the dir store inputs')
	print('---> name: the name of detected program')

def ProcessArgs(argvs):
	arg_file='' #输入的参数文件
	opts, args=getopt.getopt(argvs, 'hi:')
	for op, value in opts:
		if op=='-i':
			arg_file=value
		elif op=='-h':
			Usage()
			sys.exit()
	GetArgsFromFile(arg_file) #从文件中获取参数

def GetInputs():
	global INDIR
	global all_inputs
	files=os.listdir(INDIR)
	for eachfile in files:
		file_name=os.path.join(INDIR, eachfile)
		if(os.path.isfile(file_name)):
			all_inputs.append(file_name)
	print('All inputs: '+str(len(all_inputs)))

def Run(): #进行真正的测试
	global START
	global all_inputs
	global current_input
	global end_flag
	num_all=len(all_inputs)
	num_now=0
	for each_file in all_inputs:
		current_input=each_file
		one_order=START
		one_order=one_order.replace('@@', each_file)
		print('start detection')
		os.system(one_order)
		print('detection finish')
		num_now=num_now+1
		print("Running ---> "+str(num_now)+" : "+str(num_all))
		time.sleep(1)
	end_flag=1

def CheckProcess():
	global end_flag
	global KILL, NAME
	global current_input
	processnum=''
	oldprocessnum=''
	input_dir=NAME+'_real_deadlock'
	while not end_flag:
		readprocess='ps -ef | grep '+KILL+' | grep -v grep'
		getprocess=(os.popen(readprocess)).readlines()
		if len(getprocess)>0:
			processnum_in=(''.join(getprocess[0])).split()
			if len(processnum_in)>1 and (processnum_in[1]).isdigit():
				processnum=processnum_in[1]
				if oldprocessnum.strip() == processnum.strip():
					if not os.path.exists(input_dir):
						os.mkdir(input_dir)
					new_file_name=os.path.join(input_dir, (os.path.split(current_input))[1])
					shutil.copyfile(current_input, new_file_name)
					try:
						os.system('/usr/bin/kill -9 '+processnum)
					except Exception, e:
						print e
				oldprocessnum=processnum
		time.sleep(900)

def main():
	ProcessArgs(sys.argv[1:]) #处理参数，从文件中得到
	GetInputs()
	t=threading.Thread(target=CheckProcess, name='CheckThread')
	t.start()
	Run()
	t.join()

if __name__ == '__main__':
	main()
