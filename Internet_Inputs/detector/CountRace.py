#!/usr/bin/python
# -*- coding: UTF-8 -*-   

import os

AllRaces=[]
FileNum=0
DIR='/home/luopeng/Nginx/detector/Race'

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

CheckExist()
print len(AllRaces)
