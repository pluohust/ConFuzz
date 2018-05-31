#include "Init_Close.h"

extern map<UINT32, ThreadVecTime> AllThread;
extern size_t MaxSum;
extern int ThreadNum;
extern bool monitorendflag;

extern ofstream RaceOut;

void InitFileOutput()
{
    char filename[50];

    sprintf(filename,"RaceOut.out");
    RaceOut.open(filename);
    RaceOut.setf(ios::showbase);
}

void CloseFileOutput()
{
    RaceOut.close();
}

int Usage()
{
    cerr << "This is the invocation pintool" << endl;
    cerr << endl << KNOB_BASE::StringKnobSummary() << endl;
    return -1;
}

VOID Fini(INT32 code, VOID *v)
{
    monitorendflag=true;
}
