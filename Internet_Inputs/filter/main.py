#!/usr/bin/python
# -*- coding: UTF-8 -*-   
import cPickle
import sys
import socket
import time
import threading
import itertools
import urllib2
import subprocess
import getopt
import shutil
import os
import signal
import select
import fcntl

HOST='127.0.0.1'
PORT=8888
START=''
FILE=''
DIR=''
PROCESS=''
SHMPATH=''

def GetArgsFromFile(INPUTS):
    global HOST,PORT,START,FILE,DIR,PROCESS,SHMPATH
    
    ReadHandle=open(INPUTS,'r')
    while True:
        getoneline=ReadHandle.readline()
        if getoneline:
            if 'host:' in getoneline:
                HOST=(getoneline.split('host: '))[1]
                HOST=(HOST.rstrip()).lstrip()
            elif 'port:' in getoneline:
                PORT=(int)((getoneline.split('port: '))[1])
            elif 'start:' in getoneline:
                START=(getoneline.split('start: '))[1]
                START=(START.rstrip()).lstrip()
            elif 'file:' in getoneline:
                FILE=(getoneline.split('file: '))[1]
                FILE=(FILE.rstrip()).lstrip()
            elif 'dir:' in getoneline:
                DIR=(getoneline.split('dir: '))[1]
                DIR=(DIR.rstrip()).lstrip()
            elif 'shmpath:' in getoneline:
                SHMPATH=(getoneline.split('shmpath: '))[1]
                SHMPATH=(SHMPATH.rstrip()).lstrip()
            elif 'process:' in getoneline:
                PROCESS=(getoneline.split('process: '))[1]
                PROCESS=(PROCESS.rstrip()).lstrip()
        else:
            break
    if len(DIR)<1:
        DIR=time.strftime('%Y.%m.%d.%H',time.localtime())+'/'
    if len(START)<1 or len(FILE)<1 or len(PROCESS)<1 or len(SHMPATH)<1:
        print 'the args are not enough!'
        sys.exit()

def usage():
    print '-h help information'
    print '-i the argvs from file, and the format is that:'
    print '---> host: the host IP address, default value 127.0.0.1'
    print '---> port: the port of host, default value 80'
    print '---> start: the cmd line of server, such as \"pin -t *.so -- httpd\"'
    print '---> stop: the cmd line of stop server, such as \"apachetl stop\"'
    print '---> file: the input case file'
    print '---> process: the name of process'
    print '---> shmpath: the path of shm memory program'

def ProcessArgs(argvs): #处理输入参数
    INPUTS='' #input file name
    opts, args=getopt.getopt(argvs, 'hi:')
    for op, value in opts:
        if op=='-i':
            INPUTS=value
        elif op=='-h':
            usage()
            sys.exit()
    GetArgsFromFile(INPUTS) #从文件里获取参数

class LoadCases :
    def __init__(self,input_filename=None):
        self.input_filename=input_filename
        self.SumOfCases=0
        self.InputFileHandle=0
    
    def GetSum(self):
        with open(self.input_filename) as tf:
            temp_num=sum(1 for x in tf)
            self.SumOfCases=(temp_num-1)/2
        return self.SumOfCases
    
    def GetOneCase(self):
        data=None
        if self.InputFileHandle==0:
            self.InputFileHandle=open(self.input_filename,'r')
        try:
            data=cPickle.load(self.InputFileHandle)
            return data
        except Exception, e:
            print e
    
    def __del__(self):
        if self.InputFileHandle!=0:
            try:
                self.InputFileHandle.close()
            except Exception, e:
                print e

def SartHttpdSever(server_env):
    print'begin start server!'
    while True:
        try:
            start_httpd=subprocess.Popen(START, env=server_env, shell=True)
            time.sleep(0.01)
        except:
            time.sleep(0.01)
        is_server='ps -ef | grep '+PROCESS+' | grep -v grep'
        get_process=(os.popen(is_server)).readlines()
        if len(get_process)>0:
            break
        else:
            time.sleep(0.01)
    print str(start_httpd.pid)
    timeout_return=0
    while True:
        timeout_return=timeout_return+1
        if timeout_return>10:
            return 0
        try:
            one_connect=urllib2.urlopen('http://'+HOST+':'+str(PORT),timeout=1)
            one_connect.close()
            break
        except:
            time.sleep(0.01)
    print 'the server has started!'
    return start_httpd.pid

def StopHttpdSever():
    print 'begin stop server'
    while True:
        is_server='ps -ef | grep '+PROCESS+' | grep -v grep'
        get_process=(os.popen(is_server)).readlines()
        all_processes=''
        if len(get_process)>1:
            for i in range(0, len(get_process)):
                this_process=get_process[i]
                this_process=''.join(this_process)
                this_split=this_process.split()
                if len(this_split)>1 and (this_split[1]).isdigit():
                    all_processes=all_processes+' '+this_split[1]
            print all_processes
            try:
                os.system('/usr/bin/kill -QUIT '+all_processes)
                print 'kill one'
            except Exception, e:
                print 'can not kill process'
                os.system('/usr/bin/kill -9 '+all_processes)
            time.sleep(1)
            is_server='ps -ef | grep '+PROCESS+' | grep -v grep'
            get_process=(os.popen(is_server)).readlines()
            if len(get_process)==0:
                break
        else:
            break
    print 'the server has stopped!'

class SendCases :
    def __init__(self, host='127.0.0.1',port=80):
        self.host=host
        self.port=port
    
    def Connect(self):
        try:
            self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except Exception,e:
            print('Failed to create socket: %s' % e)
            sys.exit(1); 
        
        try:
            self.clientSocket.connect((self.host, self.port))
        except Exception, e:
            print "Connection error: %s" % e
            sys.exit(1)
#        print('Socket Connected to ' + self.host)
    
    def Send(self,InputCase):
        try:
            self.clientSocket.sendall(InputCase)
#            print "send success!"
#            print InputCase
        except Exception, e:
            print "Send error: %s" % e
            time.sleep(0.05);
    
    def Close(self):
        self.clientSocket.close()

class OneInputThread(threading.Thread) :
    def __init__(self,InputCase):
        threading.Thread.__init__(self)
        self.InputCase=InputCase
    
    def run(self):
        for each_one_input in self.InputCase:
            for i_tmp in range(0,20):
#                print "Start send!"
                sender=SendCases(host=HOST,port=PORT)
                sender.Connect()
                sender.Send(each_one_input)
                sender.Close()
                time.sleep(0.02)
#                print "End send!"

class PathProcess(object):
  def __init__(self, args, server_env = None):
    if server_env:
      self.process = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=server_env)
    else:
      self.process = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    flags = fcntl.fcntl(self.process.stdout, fcntl.F_GETFL)
    fcntl.fcntl(self.process.stdout, fcntl.F_SETFL, flags | os.O_NONBLOCK)

  def send(self, data, tail = '\n'):
    if data != 'exit':
        data = '$' + data
    self.process.stdin.write(data + tail)
    self.process.stdin.flush()

  def recv(self, t=.1, stderr=0):
    r = ''
    pr = self.process.stdout
    if stderr:
      pr = self.process.stdout
    while True:
      if not select.select([pr], [], [], 0)[0]:
        time.sleep(t)
        continue
      r = pr.read()
      return r.rstrip()
    return r.rstrip()

def storeinputs(savecount, MultiCases):
    if not os.path.exists(DIR):
        os.mkdir(DIR)
    if DIR[len(DIR)-1]!='/':
        data_filename=DIR+'/'+str(savecount)+'.log'
    else:
        data_filename=DIR+str(savecount)+'.log'
    write_filename=open(data_filename,'w')
    cPickle.dump(len(MultiCases),write_filename)
    for each_data in MultiCases:
        cPickle.dump(each_data,write_filename)
    write_filename.close()

def main():
    global SHMPATH,FILE
    ProcessArgs(sys.argv[1:]) #处理参数，从文件中得到
    shmpath=PathProcess(SHMPATH) #申请共享内存，并对路径进行处理
    getsuccess=shmpath.recv() #查看是否申请共享内存成功
    print getsuccess, len(getsuccess)
    if getsuccess[0]!='s' and getsuccess[1]!='u':
        print 'setup shm path fail!'
        sys.exit()
    shmpath.send('go!') #为获取共享内存id号进行I/O间隔
    getshmid=shmpath.recv() #获取共享内存的id号
    print getshmid, len(getshmid)
    print int(getshmid),len(str(int(getshmid)))
    server_env = os.environ.copy()
    server_env['__AFL_SHM_ID'] = getshmid
    InputCase=LoadCases(FILE)
    MaxLenOfCase=InputCase.GetSum()
    MaxLenOfCase=MaxLenOfCase/20
    savecount=0
    for i in range(0,MaxLenOfCase):
        print str(i*100/MaxLenOfCase)+'%'
        MultiCases=[]
        for j in range(0,20):
            data = InputCase.GetOneCase()
            MultiCases.append(data)
        SartHttpdSever(server_env)
        threads=[]
        for each_num1 in range(0,4):
            threads.append(OneInputThread(MultiCases))
        for each_thread in threads:
            each_thread.start()
        for each_thread in threads:
            each_thread.join()
        StopHttpdSever()
        shmpath.send('do')
        whethersave=shmpath.recv()
        print whethersave
        if whethersave[0]=='y':
            savecount=savecount+1
            storeinputs(savecount, MultiCases)
        time.sleep(1.5)
    shmpath.send('exit')
    print shmpath.recv()
    print savecount


if __name__ == '__main__':
    main()
