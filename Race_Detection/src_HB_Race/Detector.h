#include "main_basictype.h"

#ifndef HUST_DETECTOR_CGCL
#define HUST_DETECTOR_CGCL

bool CompareVC(THREADID threadid, map<UINT32, long> &OldVC, map<UINT32, long> &NewVC);
void VectorDetect(THREADID threadID, ThreadVecTime &TargetThread);

#endif
