#include "main_basictype.h"

#ifndef HUST_VECTORCLOCKS_CGCL
#define HUST_VECTORCLOCKS_CGCL

VOID ThreadStart(THREADID threadid, CONTEXT *ctxt, INT32 flags, VOID *v);
VOID ThreadFini(THREADID threadid, const CONTEXT *ctxt, INT32 code, VOID *v);
VOID BeforePthread_create(THREADID threadid);
VOID AfterPthread_join(THREADID threadid);
VOID BeforePthread_mutex_lock(ADDRINT currentlock, THREADID threadid);
VOID AfterPthread_mutex_lock(THREADID threadid);
VOID BeforePthread_mutex_trylock(ADDRINT currentlock, THREADID threadid);
VOID AfterPthread_mutex_trylock(int flag, THREADID threadid);
VOID BeforePthread_mutex_unlock(ADDRINT currentlock, THREADID threadid);
VOID BeforePthread_cond_wait(ADDRINT cond, ADDRINT mutex, THREADID threadid);
VOID AfterPthread_cond_wait(THREADID threadid);
VOID BeforePthread_cond_timedwait(ADDRINT cond, ADDRINT mutex, THREADID threadid);
VOID AfterPthread_cond_timedwait(THREADID threadid);
VOID BeforePthread_cond_signal(ADDRINT cond, THREADID threadid);
VOID BeforePthread_cond_broadcast(ADDRINT cond, THREADID threadid);

#endif
