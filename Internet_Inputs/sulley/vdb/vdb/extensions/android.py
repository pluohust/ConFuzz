import envi.cli as e_cli
#import vdb.extensions.gdbstub as ve_gdbstub
import vtrace.platforms.android as vt_android

def adb(db, line):
    '''
    Pass a command directly to the adb bridge command.
    (mostly just so you don't need another prompt)

    Usage adb <adb args>
    '''
    argv = e_cli.splitargs(line)
    db.vprint( vt_android.adbCommand('adb', *argv) )

def vdbExtension(db, trace):
    db.registerCmdExtension(adb)
    #db.registerCmdExtension(ve_gdbstub.gdbmon)

