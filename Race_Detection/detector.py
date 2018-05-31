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
DIR=''
INDIR=''
NAME=''
RACEOUT=''
KILL=''

all_inputs=[]
all_races=[]
file_num=0
end_flag=0

current_input=''

def ResultsPrint():
	global DIR, START, INDIR, NAME
	global all_races, file_num
	
	print(DIR)
	print(START)
	print(INDIR)
	print('Races count: '+str(file_num))
	
	writehandle=open(NAME+'.out', 'w')
	writehandle.write('Races count: '+str(file_num)+'\n')
	writehandle.write('------------------------------\n\n')
	for eachone in all_races:
		writehandle.write(eachone+'\n\n')
	writehandle.close()
	time.sleep(0.01)

def GetArgsFromFile(arg_file):
	global DIR, START, INDIR, NAME, RACEOUT, KILL
	
	readhandle=open(arg_file, 'r')
	while True:
		getoneline=readhandle.readline()
		if getoneline:
			if 'start: ' in getoneline:
				START=((getoneline.split('start: '))[1]).strip()
			elif 'indir: ' in getoneline:
				INDIR=((getoneline.split('indir: '))[1]).strip()
			elif 'dir: ' in getoneline:
				DIR=((getoneline.split('dir: '))[1]).strip()
			elif 'name: ' in getoneline:
				NAME=((getoneline.split('name: '))[1]).strip()
			elif 'raceout: ' in getoneline:
				RACEOUT=((getoneline.split('raceout: '))[1]).strip()
			elif 'kill: ' in getoneline:
				KILL=((getoneline.split('kill: '))[1]).strip()
		else:
			break
	readhandle.close()
	if len(DIR)<1:
		DIR=time.strftime('%Y.%m.%d.%H',time.localtime())+'/'
	if not os.path.exists(DIR):
		os.mkdir(DIR)
	if len(START)<1 or len(INDIR)<1 or len(NAME)<1 or len(RACEOUT)<1 or len(KILL)<1:
		print('the args are not enough in'+arg_file+'!')
		sys.exit()

def Usage():
	print('-h help information')
	print('-i the argvs from file, and the format is that:')
	print('---> start: the cmd line of server, such as \"pin -t *.so -- httpd\"')
	print('---> indir: the inputs dir')
	print('---> dir: the dir store inputs')
	print('---> name: the name of detected program')
	print('---> raceout: the output file of race results')

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

def RaceCheck():
	global DIR, RACEOUT
	global all_races, file_num
	global current_input
	if not os.path.isfile(RACEOUT):
		print('error: no race result file!')
		return
	racehandle=open(RACEOUT, 'r')
	is_store=0
	each_pair=''
	while True:
		oneline=racehandle.readline()
		if oneline:
			oneline.strip()
			if len(oneline)>1:
				each_pair=each_pair+'\n'+oneline
				each_pair.strip()
			else:
				if each_pair not in all_races:
					all_races.append(each_pair)
					is_store=1
				each_pair=''
		else:
			break
	racehandle.close()
	time.sleep(0.01)
	if is_store:
		file_num=file_num+1
		new_file_name=os.path.join(DIR, (os.path.split(current_input))[1])
		try:
			shutil.copyfile(current_input, new_file_name)
		except EXception, e:
			print(e)
		time.sleep(0.01)
		
	os.remove(RACEOUT)
	time.sleep(0.01)

def Run(): #进行真正的测试
	global START
	global all_inputs
	global current_input
	global end_flag
	for each_file in all_inputs:
		current_input=each_file
		one_order=START
		one_order=one_order.replace('@@', each_file)
		print('start detection')
		os.system(one_order)
		print('detection finish')
		time.sleep(3)
		RaceCheck()
		time.sleep(3)
	end_flag=1

def CheckProcess():
	global end_flag
	global KILL, NAME
	global current_input
	processnum=''
	oldprocessnum=''
	input_dir=NAME+'_deadlock'
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
	ResultsPrint()
	t.join()

if __name__ == '__main__':
	main()
