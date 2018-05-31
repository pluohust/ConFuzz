PREFIX     ?= /usr/local
BIN_PATH    = $(PREFIX)/bin
HELPER_PATH = $(PREFIX)/lib/afl
DOC_PATH    = $(PREFIX)/share/doc/afl
MISC_PATH   = $(PREFIX)/share/afl

PROGS       = afl-gcc

CFLAGS     ?= -O3 -funroll-loops
CFLAGS     += -Wall -D_FORTIFY_SOURCE=2 -g -Wno-pointer-sign \
	      -DAFL_PATH=\"$(HELPER_PATH)\" -DDOC_PATH=\"$(DOC_PATH)\" \
	      -DBIN_PATH=\"$(BIN_PATH)\"

COMM_HDR    = alloc-inl.h config.h debug.h types.h

all: $(PROGS) afl-as

afl-gcc: afl-gcc.c $(COMM_HDR)
	$(CC) $(CFLAGS) $@.c -o $@ $(LDFLAGS)
	set -e; for i in afl-g++; do ln -sf afl-gcc $$i; done

afl-as: afl-as.c afl-as.h $(COMM_HDR)
	$(CC) $(CFLAGS) $@.c -o $@ $(LDFLAGS)
	ln -sf afl-as as

.NOTPARALLEL: clean

clean:
	rm -f afl-as as afl-gcc afl-g++  *.o *~ a.out test .test test-instr .test-instr0 .test-instr1
