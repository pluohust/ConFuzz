#include "monitor_shared_memory.h"

using namespace std::tr1;

extern set<ADDRINT> ShareVarAddress;
extern map<UINT32, ThreadVecTime> AllThread;
extern bool startmallocmonitor;
extern vector<ShareAddreeStruct> MallocVec;
extern PIN_LOCK lock;
extern PIN_LOCK shareaddrlock;
extern map<THREADID, USIZE> MallocSize, CallocSize;
extern map<THREADID, USIZE> MallocThread;
extern map<THREADID, USIZE> CallocThread;

extern ofstream RaceOut;

extern map<THREADID, Myloopqueue<ADDRINT> > RecordLastCallIns;

VOID GetShareAddress() //if you know the address of global variables, please store them in address file.
{
    FILE *faddress;
    char oneline[50];
    ADDRINT oneaddress;
    int i;
    if((faddress=fopen("./address","rt"))==NULL)
    {
        return;
    }
    while(!feof(faddress))
    {
        oneaddress=0;
        fgets(oneline,50,faddress);
        if('\0'==oneline[0])
            break;
        for(i=0;' '!=oneline[i];i++);
        i=i+3;
        while(('\0'!=oneline[i])&&(i<50))
        {
            if((oneline[i]>='0')&&(oneline[i]<='9'))
            {
                oneaddress=oneaddress*16;
                oneaddress=oneaddress+oneline[i]-'0';
            }
            else if((oneline[i]>='a')&&(oneline[i]<='f'))
            {
                oneaddress=oneaddress*16;
                oneaddress=oneaddress+10+oneline[i]-'a';
            }
            else if((oneline[i]>='A')&&(oneline[i]<='F'))
            {
                oneaddress=oneaddress*16;
                oneaddress=oneaddress+10+oneline[i]-'A';
            }
            i++;
        }
        ShareVarAddress.insert(oneaddress);
    }
    fclose(faddress);
}

BOOL IsGlobalVariable(ADDRINT address) //identify if the address is a shared-memory location
{
    if(ShareVarAddress.find(address)!=ShareVarAddress.end()) //if it is in ShareVarAddress
        return true;
    else if(!MallocVec.empty()) //else if it is a heap location and use binary chop algorithm
    {
        int low=0;
        int high=MallocVec.size() - 1;
        int mid=(low+high)/2;
        if((MallocVec[0]).address_name > address)
            return false;
        else if((MallocVec[high]).address_name <= address)
        {
            if((MallocVec[high]).address_name+(MallocVec[high]).address_size > address)
            {
                ShareVarAddress.insert(address);
                return true;
            }
            else
                return false;
        }
        while (low < high)
        {
            mid=(low+high)/2;
            if((MallocVec[mid]).address_name > address)
                high=mid-1;
            else if((MallocVec[mid]).address_name < address)
                low=mid+1;
            else
                break;
        }
        if((MallocVec[mid]).address_name > address)
        {
            if(((MallocVec[mid-1]).address_name <= address)&&((MallocVec[mid-1]).address_name + (MallocVec[mid-1]).address_size) > address)
            {
                ShareVarAddress.insert(address);
                return true;
            }
            else
                return false;
        }
        else if((MallocVec[mid]).address_name < address)
        {
            if((MallocVec[mid]).address_name + (MallocVec[mid]).address_size> address)
            {
                ShareVarAddress.insert(address);
                return true;
            }
            else
                return false;
        }
        else
        {
            ShareVarAddress.insert(address);
            return true;
        }
    }
    return false;
}

VOID RecordMemRead(VOID * ip, VOID * addr, UINT32 size, THREADID threadid)
{
    PIN_GetLock(&lock, threadid+1);
    if(IsGlobalVariable((ADDRINT)addr))
    {
        unordered_map<ADDRINT, SharedMemoryAccessInf>::iterator mapforsharedmemory;
        map<UINT32, ThreadVecTime>::iterator ITforAllThread;
        ITforAllThread=AllThread.find(threadid);
        if(AllThread.end()==ITforAllThread)
        {
            PIN_ReleaseLock(&lock);
            return;
        }
        
        ((ITforAllThread->second).ListAddress)->Accessflag=true; //for detect
        
        mapforsharedmemory=(((ITforAllThread->second).ListAddress)->SharedLocation).find((ADDRINT)addr);
        if(mapforsharedmemory==(((ITforAllThread->second).ListAddress)->SharedLocation).end()) // a new address
        {
            SharedMemoryAccessInf tmpSharedMemoryAccessInf;
            tmpSharedMemoryAccessInf.Rstatus=true;
            tmpSharedMemoryAccessInf.Wstatus=false;
            tmpSharedMemoryAccessInf.InsR.insert((ADDRINT)ip);
            (((ITforAllThread->second).ListAddress)->SharedLocation).insert(pair<ADDRINT, SharedMemoryAccessInf>((ADDRINT)addr,tmpSharedMemoryAccessInf));
        }
        else // there is access to this address before
        {
            (mapforsharedmemory->second).Rstatus=true;
            (mapforsharedmemory->second).InsR.insert((ADDRINT)ip);
        }
    }
    PIN_ReleaseLock(&lock);
}

VOID RecordMemWrite(VOID * ip, VOID * addr, UINT32 size, THREADID threadid)
{
    PIN_GetLock(&lock, threadid+1);
    if(IsGlobalVariable((ADDRINT)addr))
    {
        unordered_map<ADDRINT, SharedMemoryAccessInf>::iterator mapforsharedmemory;
        map<UINT32, ThreadVecTime>::iterator ITforAllThread;
        ITforAllThread=AllThread.find(threadid);
        if(AllThread.end()==ITforAllThread)
        {
            PIN_ReleaseLock(&lock);
            return;
        }
        
        ((ITforAllThread->second).ListAddress)->Writeflag=true; //for detect
        ((ITforAllThread->second).ListAddress)->Accessflag=true;
        
        mapforsharedmemory=(((ITforAllThread->second).ListAddress)->SharedLocation).find((ADDRINT)addr);
        if(mapforsharedmemory==(((ITforAllThread->second).ListAddress)->SharedLocation).end()) // a new address
        {
            SharedMemoryAccessInf tmpSharedMemoryAccessInf;
            tmpSharedMemoryAccessInf.Rstatus=false;
            tmpSharedMemoryAccessInf.Wstatus=true;
            tmpSharedMemoryAccessInf.InsW.insert((ADDRINT)ip);
            (((ITforAllThread->second).ListAddress)->SharedLocation).insert(pair<ADDRINT, SharedMemoryAccessInf>((ADDRINT)addr,tmpSharedMemoryAccessInf));
        }
        else // there is access to this address before
        {
            (mapforsharedmemory->second).Wstatus=true;
            (mapforsharedmemory->second).InsW.insert((ADDRINT)ip);
        }
    }
    PIN_ReleaseLock(&lock);
}

IMG GetImgByIns(INS ins)
{
    IMG img = IMG_Invalid();
    RTN rtn = INS_Rtn(ins);
    if (RTN_Valid(rtn))
    {
        SEC sec = RTN_Sec(rtn);
        if (SEC_Valid(sec))
        {
          img = SEC_Img(sec);
        }
    }
    return img;
}

VOID RecordCall(VOID * ip, THREADID threadid)
{
    PIN_GetLock(&lock, threadid+1);
    if(!startmallocmonitor)
    {
        map<THREADID, Myloopqueue<ADDRINT> >::iterator findcall;
        findcall=RecordLastCallIns.find(threadid);
        if(findcall==RecordLastCallIns.end())
        {
            Myloopqueue<ADDRINT> tmpqueue;
            tmpqueue.push((ADDRINT)ip);
            RecordLastCallIns[threadid]=tmpqueue;
        }
        else
        {
            (findcall->second).push((ADDRINT)ip);
        }
    }
    PIN_ReleaseLock(&lock);
}

VOID Instruction(INS ins, VOID *v)
{
    if(INS_IsCall(ins))
        INS_InsertPredicatedCall(ins, IPOINT_BEFORE, (AFUNPTR)RecordCall, IARG_INST_PTR, IARG_THREAD_ID, IARG_END);
    else
    {
        if((!INS_IsMemoryRead(ins)) && (!INS_IsMemoryWrite(ins)))
            return;
        if (INS_IsStackRead(ins) || INS_IsStackWrite(ins))
            return;
    /*    IMG img = GetImgByIns(ins);
        if (IMG_Valid(img) && IMG_Name(img).find("bugs") == std::string::npos)
            return;*/

        UINT32 memOperands = INS_MemoryOperandCount(ins);

        for (UINT32 memOp = 0; memOp < memOperands; memOp++)
        {
            if (INS_MemoryOperandIsRead(ins, memOp))
            {
                INS_InsertPredicatedCall(ins, IPOINT_BEFORE, (AFUNPTR)RecordMemRead, IARG_INST_PTR, IARG_MEMORYOP_EA, memOp, IARG_MEMORYREAD_SIZE, IARG_THREAD_ID, IARG_END);
            }
            if (INS_MemoryOperandIsWritten(ins, memOp))
            {
                INS_InsertPredicatedCall(ins, IPOINT_BEFORE, (AFUNPTR)RecordMemWrite, IARG_INST_PTR, IARG_MEMORYOP_EA, memOp, IARG_MEMORYWRITE_SIZE, IARG_THREAD_ID, IARG_END);
            }
        }
    }
}

VOID BeforeSprintf(ADDRINT funcflag, ADDRINT dest, ADDRINT source, ADDRINT length, const CHAR * filename, THREADID threadid)
{
/*    PIN_GetLock(&shareaddrlock, threadid+1);
    if((funcflag==8801) || (funcflag==8802) || (funcflag==8803) || (funcflag==8808))
    {
        string codeinf_DEST("DEST|");
        string codeinf_SOURCE("SOURCE|");
        string codeinf_LENGTH("LENGTH|");
        string codeinf(filename);
        switch(funcflag)
        {
            case 8808:
//                string codeinf(filename);
//                vector<ShareAddreeStruct>::iterator ittmp;
                for(ittmp=MallocVec.begin();ittmp!=MallocVec.end();ittmp++)
                    cout<<hex<<"&& "<<ittmp->address_name<<dec<<" "<<ittmp->address_size<<endl;
//                MallocVec.push_back((ShareAddreeStruct) {dest, (USIZE)source});
                cout<<"@@@ "<<hex<<dest<<" "<<dec<<(USIZE)source<<endl;
                for(ittmp=MallocVec.begin();ittmp!=MallocVec.end();ittmp++)
                    cout<<hex<<"&& "<<ittmp->address_name<<dec<<" "<<ittmp->address_size<<endl;
//                sort(MallocVec.begin(), MallocVec.end(), less<ShareAddreeStruct>());
                break;
        }
    }
    PIN_ReleaseLock(&shareaddrlock);*/
}

VOID BeforeMalloc(ADDRINT size, THREADID threadid)
{
    PIN_GetLock(&shareaddrlock, threadid+1);
    map<THREADID, Myloopqueue<ADDRINT> >::iterator findlastcall;
    findlastcall=RecordLastCallIns.find(threadid);
    if((!startmallocmonitor) && (findlastcall!=RecordLastCallIns.end()))
    {
        string filename;
        INT32 line;
        PIN_LockClient();
        int i=1;
        while(!(findlastcall->second).isEmpty())
        {
            ADDRINT ip=(findlastcall->second).top();
            PIN_GetSourceLocation(ip, NULL, &line, &filename);
            if(line>1)
            {
//                RaceOut<<"***"<<filename<<":"<<line<<endl;
                startmallocmonitor=true;
//                (findlastcall->second).cleanall();
//                break;
            }
            else
            {
//                RaceOut<<"***"<<i<<endl;
                i++;
            }
            (findlastcall->second).poptop();
        }
        PIN_UnlockClient();
    }
    if(startmallocmonitor)
    {
        MallocSize[threadid]=size;
    }
    PIN_ReleaseLock(&shareaddrlock);
}

VOID AfterMalloc(ADDRINT ret,THREADID threadid)
{
    PIN_GetLock(&shareaddrlock, threadid+1);
    if(startmallocmonitor)
    {
        map<THREADID, USIZE>::iterator mallocfinder;
        mallocfinder=MallocSize.find(threadid);
        if(mallocfinder==MallocSize.end())
        {
            PIN_ReleaseLock(&shareaddrlock);
            return;
        }
        MallocVec.push_back((ShareAddreeStruct) {(ADDRINT)ret, (USIZE)(mallocfinder->second)});
        sort(MallocVec.begin(), MallocVec.end(), less<ShareAddreeStruct>());
        vector<ShareAddreeStruct>::iterator ittmp;
//        MallocSize.erase(mallocfinder);
    }
    PIN_ReleaseLock(&shareaddrlock);
}

VOID BeforeCalloc(ADDRINT num, ADDRINT size, THREADID threadid)
{
    PIN_GetLock(&shareaddrlock, threadid+1);
    if(startmallocmonitor)
    {
        CallocSize[threadid]=num*size;
    }
    PIN_ReleaseLock(&shareaddrlock);
}

VOID AfterCalloc(ADDRINT ret,THREADID threadid)
{
    PIN_GetLock(&shareaddrlock, threadid+1);
    if(startmallocmonitor)
    {
        map<UINT32, USIZE>::iterator callocfinder;
        callocfinder=CallocSize.find(threadid);
        if(callocfinder==CallocSize.end())
        {
            PIN_ReleaseLock(&shareaddrlock);
            return;
        }
        MallocVec.push_back((ShareAddreeStruct) {ret, callocfinder->second});
        sort(MallocVec.begin(), MallocVec.end(), less<ShareAddreeStruct>());
//        CallocSize.erase(callocfinder);
    }
    PIN_ReleaseLock(&shareaddrlock);
}

VOID BeforeFree(ADDRINT address, THREADID threadid)
{
    PIN_GetLock(&shareaddrlock, threadid+1);
    vector<ShareAddreeStruct>::iterator p;
    set<ADDRINT>::iterator shareaddress_it;
    for(p=MallocVec.begin(); p!=MallocVec.end(); p++)
    {
        if(address==p->address_name)
        {
            for(shareaddress_it=ShareVarAddress.begin();shareaddress_it!=ShareVarAddress.end();shareaddress_it++)
            {
                if((*shareaddress_it>=p->address_name)&&(*shareaddress_it<(p->address_name+p->address_size)))
                {
                    ShareVarAddress.erase(shareaddress_it); //remove the old shared-memory locations in the free heap memory
                }
            }
            MallocVec.erase(p);
            break;
        }
    }
    PIN_ReleaseLock(&shareaddrlock);
}

