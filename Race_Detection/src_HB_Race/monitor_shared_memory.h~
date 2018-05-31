#include "main_basictype.h"

#ifndef HUST_MONITOR_SHARED_MEMORY_CGCL
#define HUST_MONITOR_SHARED_MEMORY_CGCL

VOID GetShareAddress();
BOOL IsGlobalVariable(ADDRINT address);
VOID RecordMemRead(VOID * ip, VOID * addr, UINT32 size, THREADID threadid);
VOID RecordMemWrite(VOID * ip, VOID * addr, UINT32 size, THREADID threadid);
VOID Instruction(INS ins, VOID *v);
VOID BeforeMalloc(ADDRINT size, THREADID threadid, VOID *imgname);
VOID AfterMalloc(ADDRINT ret,THREADID threadid, VOID *imgname);
VOID BeforeSprintf(ADDRINT funcflag, ADDRINT dest, ADDRINT source, ADDRINT length, const CHAR * filename, THREADID threadid);
VOID BeforeCalloc(ADDRINT num, ADDRINT size, THREADID threadid);
VOID AfterCalloc(ADDRINT ret,THREADID threadid);
VOID BeforeFree(ADDRINT address, THREADID threadid);
VOID Beforegettimeofday();

#endif
