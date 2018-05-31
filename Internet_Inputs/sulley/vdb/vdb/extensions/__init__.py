import os
import imp
import traceback

__all__ = ['loadExtensions','windows','i386','darwin','amd64','gdbstub','arm','android']

'''
A package to contain all the extended functionality for platform specific
commands and modules.
'''

def loadExtensions(vdb, trace):
    '''
    Actually load all known extensions here.
    '''
    plat = trace.getMeta('Platform').lower()
    arch = trace.getMeta('Architecture').lower()

    if plat in __all__:
        mod = __import__('vdb.extensions.%s' % plat, 0, 0, 1)
        mod.vdbExtension(vdb, trace)

    if arch in __all__:
        mod = __import__('vdb.extensions.%s' % arch, 0, 0, 1)
        mod.vdbExtension(vdb, trace)

    extdir = os.getenv('VDB_EXT_PATH')

    if extdir != None:

        for dirname in extdir.split(';'):

            if not os.path.isdir(dirname):
                vdb.vprint('Invalid VDB_EXT_PATH dir: %s' % dirname)
                continue

            for fname in os.listdir(dirname):
                if not fname.endswith('.py'):
                    continue

                # Build code objects from the module files
                mod = imp.new_module('vdb_ext')
                filepath = os.path.join(dirname, fname)
                filebytes = file( filepath, 'r' ).read()
                mod.__file__ = filepath
                try:
                    exec filebytes in mod.__dict__
                    mod.vdbExtension(vdb, trace)
                except Exception, e:
                    vdb.vprint( traceback.format_exc() )
                    vdb.vprint('Extension Error: %s' % filepath)

