//There are some types that all call use.
#include <vector>
#include <string>
#include <map>
#include <tr1/unordered_map>
#include <set>
#include <vector>
#include <queue>
#include <stdint.h>
#include <list>
#include <pthread.h>
#include <map>
#include <algorithm>
#include <string.h>
#include <iostream>
#include <fstream>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include "pin.H"

#ifndef HUST_BASICTYPE_CGCL
#define HUST_BASICTYPE_CGCL

#define DEST 1
#define SOURCE 2
#define LENGTH 3

using namespace std::tr1;

template <typename T>
class Myloopqueue{
private:
    T *queue;//存储用的数组
    int capacity;//存放个数
    int head;//指向队首
    int tail;//指向队尾
public:
    Myloopqueue(int a){
        head=0;
        tail=0;
        capacity=a;
        queue = new T[capacity];
    }
    Myloopqueue(){
        head=0;
        tail=0;
        capacity=30;
        queue = new T[capacity];
    }
    ~Myloopqueue(){
        delete[] queue;
    }
    bool isEmpty(){
        if (head == tail)
            return true;
        else
            return false;
    }
    int getSize(){
        return (tail - head + capacity) % capacity;
    }
    void push(T a){
        queue[tail] = a;
        tail = (tail + 1) % capacity;
        if ((tail - head + capacity) % capacity == 0)
            head++;
        head=head % capacity;
    }
    void poptop(){
        tail = (tail - 1 + capacity) % capacity;
    }
    T top(){
        return queue[(tail-1+capacity)%capacity];
    }
};

struct RecordType //Record the necessary information to the detector
{
    int style;
    UINT32 threadID;
    ADDRINT object;
};

struct RecordCond //Record the necessary information to the conditional variable
{
    int style;
    UINT32 threadID;
    ADDRINT cond;
    ADDRINT mutex;
};

struct ShareAddreeStruct //This is the share memory space address
{
    ADDRINT address_name;
    USIZE address_size;
    
    bool operator <(const ShareAddreeStruct& rhs) const
    {
        return address_name < rhs.address_name;
    }
    
    bool operator >(const ShareAddreeStruct& rhs) const
    {
        return address_name > rhs.address_name;
    }
};

struct ResultInf
{
    long number;
    string codeinf;
};

struct LockInf //Each share address' lock information
{
    int R;
    int W;
    std::vector<ADDRINT> lockID;
};

struct EachAddressInf //Each share address details
{
    bool RWflag;
    int sumR, sumW;
    int unlockR, unlockW;
    UINT32 threadID;
    ADDRINT address;
    std::vector<LockInf> lock;
    struct EachAddressInf *next;
};

struct MemoryData //Each memory address information
{
    bool SignalStatus;
    ADDRINT SignalAddress;
    std::vector<ADDRINT> veclock;
    struct EachAddressInf *EachShareAddress;
    struct MemoryData *next;
    std::vector<MemoryData *> Prior, Following;
};

struct ThreadInf //Each thread information
{
    int status; //ThreadStart is 1;
    UINT32 threadID;
    UINT32 fartherthreadID;
    struct MemoryData *data;
    struct ThreadInf *next;
};

struct ThreadParent //The relationship between the farther and child
{
    bool liveflag;
    THREADID fatherthreadid;
};

struct CreateThreadInf
{
    UINT32 threadID;
    struct MemoryData *data;
};

struct RtnNameNumber //Get the function name
{
    string RtnName;
    long InsNumber;
};

struct RtnAddress //Get the last access address to get the code address
{
    string ImgName;
    ADDRINT MemoryAddress;
};

struct SharedMemoryAccessInf //This is just an access but store enough information
{
    bool Rstatus, Wstatus;
    set<ADDRINT> InsR;
    set<ADDRINT> InsW;
//    long Rcount, Wcount;
//    ADDRINT the_ins_in_memory_r;
//    ADDRINT the_ins_in_memory_w;
};

struct RWVecTime
{
    //flag
    bool Writeflag;
    bool Accessflag;
    //other information
    string SynName;
    map<UINT32, long> VecTime;
    //store the related function information
    unordered_map<ADDRINT, SharedMemoryAccessInf> SharedLocation;
};

struct ThreadVecTime
{
    list<struct RWVecTime>::iterator ListAddress;
    list<struct RWVecTime> VecTimeList;
};
#endif
