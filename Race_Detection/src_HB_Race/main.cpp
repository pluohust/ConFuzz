#include "main_basictype.h"
#include "monitor_shared_memory.h"
#include "Detector.h"
#include "VectorClocks.h"
#include "Init_Close.h"
#include "monitor_function.h"

using namespace std;
using namespace std::tr1;

set<ADDRINT> ShareVarAddress; //Record the address
map<THREADID, ThreadParent> ThreadMapParent; //Record the relationship between child and father
map<THREADID, USIZE> MallocSize, CallocSize; //Record the malloc and calloc information
map<THREADID, USIZE> MallocThread, CallocThread;
map<OS_THREAD_ID, THREADID> ThreadIDInf; //Record the thread ID information
bool startmallocmonitor=false; //The flag to start malloc fuction and recod heap memory locations
PIN_LOCK lock, shareaddrlock;
map<THREADID, RecordCond> VecWait; //Record conditional variables
map<THREADID, ADDRINT> AfterLockInf; //Record lock
bool monitorendflag=false, realendflag=false; //the end flags

map<UINT32, ThreadVecTime> AllThread; //The whole information
map<ADDRINT, map<UINT32, long> > SignalVecTime; //Condition vec time
map<ADDRINT, map<UINT32, long> > LockVecTime; //Lock vec time
map<UINT32, queue<map<UINT32, long> > > CreateThreadVecTime; //Record the father vec time
map<UINT32, map<UINT32, long> > FiniThreadVecTime; //record the finish vec time

map<UINT32, queue<ADDRINT> > recode_ins_address; //recode the ins address in memory

map<THREADID, Myloopqueue<ADDRINT> > RecordLastCallIns; //record the last call ins

ofstream RaceOut; //race

set<string> Result_RaceOut;

int ThreadNum=0; //thread count
int Race_Warnings=0;
long ConNumFrames=0; //the count of concurrent frames
long NumAnalysis=0; //the count of analysis

vector<ShareAddreeStruct> MallocVec; //store Malloc address
size_t MaxSum=0; //memory used

int main(int argc, char * argv[])
{
    if (PIN_Init(argc, argv))
        return Usage();
    PIN_InitLock(&lock);
    PIN_InitLock(&shareaddrlock);
    PIN_InitSymbols();
    
    InitFileOutput();
    GetShareAddress();
    
    IMG_AddInstrumentFunction(ImageLoad, 0);
    INS_AddInstrumentFunction(Instruction, 0);
    PIN_AddFiniFunction(Fini, 0);

    PIN_AddThreadStartFunction(ThreadStart, 0);
    PIN_AddThreadFiniFunction(ThreadFini, 0);

    PIN_StartProgram();

    CloseFileOutput();
    return 0;
}
