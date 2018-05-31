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
COUNT='count.log'

AllRaces=[]
FileNum=0

RecordHandle=0

def GetArgsFromFile(INPUTS):
    global HOST,PORT,START,STOP,FILE,DIR,PROCESS,SHMPATH
    
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
            elif 'process:' in getoneline:
                PROCESS=(getoneline.split('process: '))[1]
                PROCESS=(PROCESS.rstrip()).lstrip()
            elif 'count:' in getoneline:
                COUNT=(getoneline.split('count: '))[1]
                COUNT=(COUNT.rstrip()).lstrip()
        else:
            break
    ReadHandle.close()
    if len(DIR)<1:
        DIR=time.strftime('%Y.%m.%d.%H',time.localtime())+'/'
    if not os.path.exists(DIR):
        os.mkdir(DIR)
    if len(START)<1 or len(FILE)<1 or len(PROCESS)<1:
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

def GetCount():
    global COUNT
    CountHandle=None
    try:
        CountHandle=open(COUNT, 'r')
        racecount=int(CountHandle.readline().strip())
        CountHandle.close()
    except Exception, e:
        print 'No Race Count'
        racecount=0
        if CountHandle:
            CountHandle.close()
    return racecount

def StoreCount(racecount):
    global COUNT
    CountHandle=open(COUNT, 'w')
    CountHandle.write(str(racecount))
    CountHandle.close()

def CheckExist():
    global FileNum,DIR,AllRaces
    files = os.listdir(DIR)
    for each in files:
        if each[0]!='.' and os.path.isdir(os.path.join(DIR, each)):
            FileNum=FileNum+1
            RaceHandle=open(os.path.join(DIR, each, 'RaceOut.out'), 'r')
            EachPair=''
            while True:
                eachone=RaceHandle.readline()
                if eachone:
                    eachone=eachone.strip()
                    if len(eachone)>1:
                        EachPair=EachPair+'\n'+eachone
                        EachPair=EachPair.strip()
                    else:
                        if EachPair not in AllRaces:
                            AllRaces.append(EachPair)
                        EachPair=''
                else:
                    break
            RaceHandle.close()

def GetInputs():
    global FILE
    allinputs=[]
    files = os.listdir(FILE)
    for each in files:
        if(os.path.isfile(FILE + '/' + each)):
            allinputs.append(FILE + '/' + each)
    return allinputs

def SartHttpdSever():
    print'begin start server!'
    while True:
        try:
            start_httpd=subprocess.Popen(START, shell=True)
            time.sleep(5)
        except:
            time.sleep(5)
        is_server='ps -ef | grep '+PROCESS+' | grep -v grep'
        get_process=(os.popen(is_server)).readlines()
        if len(get_process)>0:
            break
        else:
            time.sleep(5)
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
            time.sleep(5)
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
                os.system('/usr/bin/kill -9 '+all_processes)
                print 'kill one'
            except Exception, e:
                print 'can not kill process'
            time.sleep(10)
            is_server='ps -ef | grep '+PROCESS+' | grep -v grep'
            get_process=(os.popen(is_server)).readlines()
            if len(get_process)==0:
                break
        else:
            break
    print 'the server has stopped!'

class SendCases :
    def __init__(self, host='127.0.0.1',port=8888):
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
        global HOST, PORT
        for each_one_input in self.InputCase:
            for i_tmp in range(0,1):
#                print "Start send!"
                sender=SendCases(host=HOST,port=PORT)
                sender.Connect()
                sender.Send(each_one_input)
                sender.Close()
                time.sleep(0.1)
#                print "End send!"

def storeinputs(FileDir, MultiCases):
    if not os.path.exists(FileDir):
        os.mkdir(FileDir)
    if FileDir[len(FileDir)-1]!='/':
        data_filename=FileDir+'/'+'input.log'
    else:
        data_filename=FileDir+'input.log'
    write_filename=open(data_filename,'w')
    cPickle.dump(len(MultiCases),write_filename)
    for each_data in MultiCases:
        cPickle.dump(each_data,write_filename)
    write_filename.close()

def RaceCheck(MultiCases):
    global AllRaces, FileNum, RecordHandle
    RaceHandle=open('./RaceOut.out', 'r')
    EachPair=''
    IsStore=0
    while True:
        eachone=RaceHandle.readline()
        if eachone:
            eachone=eachone.strip()
            if len(eachone)>1:
                EachPair=EachPair+'\n'+eachone
                EachPair=EachPair.strip()
            else:
                if EachPair not in AllRaces:
                    AllRaces.append(EachPair)
                    IsStore=1
                EachPair=''
        else:
            break
    RaceHandle.close()
    time.sleep(0.01)
    if IsStore:
        FileNum=FileNum+1
        if DIR[len(DIR)-1]!='/':
            FileDir=DIR+'/'+str(FileNum)
        else:
            FileDir=DIR+str(FileNum)
        if not os.path.exists(FileDir):
            os.mkdir(FileDir)
        if FileDir[len(FileDir)-1]!='/':
            RaceName=FileDir+'/RaceOut.out'
        else:
            RaceName=FileDir+'RaceOut.out'
        try:
            shutil.move('./RaceOut.out', RaceName)
        except Exception, e:
            print e
        time.sleep(0.01)
        storeinputs(FileDir, MultiCases)
        time.sleep(0.01)
    else:
        os.remove('./RaceOut.out')
    print 'All Races:'+str(len(AllRaces))
    RecordHandle.write(str(len(AllRaces))+'\n')

def main():
    global FILE, RecordHandle
    RecordHandle=open('./RaceChange.txt', 'w')
    ProcessArgs(sys.argv[1:]) #处理参数，从文件中得到
    racecount=GetCount()
    racecount=racecount+1
    CheckExist()
    allinputs=GetInputs()
    allcount=len(allinputs)
    for eachcount in range(racecount, allcount+1):
        StoreCount(eachcount)
        inputfile=os.path.join(FILE, str(eachcount)+'.log')
        if not os.path.isfile(inputfile):
            print 'The input file wrong'
            break
        MultiCases=[]
        InputHandle=open(inputfile, 'r')
        NumOfInputs=cPickle.load(InputHandle)
        for i in range(0, NumOfInputs):
            data=cPickle.load(InputHandle)
            MultiCases.append(data)
        InputHandle.close()
        start_httpd=SartHttpdSever()
        threads=[]
        for each_num1 in range(0,2):
            threads.append(OneInputThread(MultiCases))
        for each_thread in threads:
            each_thread.start()
        for each_thread in threads:
            each_thread.join()
        time.sleep(1)
        StopHttpdSever()
        print str(eachcount*100/allcount), '%', ' : ', str(eachcount), '---', str(allcount)
        print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        time.sleep(6)
        RaceCheck(MultiCases)
        time.sleep(2)
    RecordHandle.close()
#        if stopcount>2:
#            break

if __name__ == '__main__':
    main()
