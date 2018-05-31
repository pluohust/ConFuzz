EPY=epydoc
BASEDIR=$(CURDIR)
OUTPUTDIR=$(BASEDIR)/docs


help:
		@echo 'Makefile for a VDB                                                          '
		@echo '                                                                            '
		@echo 'Usage:                                                                	   '
		@echo '   make docs-all                    Generate epydocs for all modules        '
		@echo '   make docs mod={MODULE}               Generate epydocs for specific modules   '
		@echo '   make test                        Run tests (not implemented yet)         '
		@echo '                                                                            '


docs-all: 
		$(EPY) --html -o $(OUTPUTDIR)/all Elf envi vdb visgraph vqt vtrace vwidget

docs:
		@echo "Generating docs for $(ARG)"
		$(EPY) --html -o $(OUTPUTDIR)/doc_${mod} ${mod}

test:
		@echo 'No tests yet!'

.PHONY: help docs-all docs test
