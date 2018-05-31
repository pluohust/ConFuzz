'''
Run all the unit tests....
'''

import basictest
import graphdbtest
import pathtest

def runTestModule(mod):
    for name in dir(mod):
        if name.startswith('vgtest'):
            testfunc = getattr(mod, name)
            print 'Running %s...' % name
            testfunc()

if __name__ == '__main__':
    runTestModule(basictest)
    runTestModule(graphdbtest)
    runTestModule(pathtest)
