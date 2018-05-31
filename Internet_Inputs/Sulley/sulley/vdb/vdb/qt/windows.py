'''
The heart of the new VDB QT gui!
'''
from PyQt4 import QtCore, QtGui

import vdb
import vtrace

#import vqt.cli as vq_cli
import vqt.main as vq_main
import vqt.qpython as vq_python
import vqt.application as vq_app

import vtrace.qt as vtrace_qt

import envi.qt as envi_qt
import envi.qt.memory as e_mem_qt


class VdbMemoryWindow(e_mem_qt.VQMemoryWindow, vtrace.Notifier):

    def __init__(self, db, parent=None):
        t = vdb.VdbTrace(db)
        e_mem_qt.VQMemoryWindow.__init__(self, t, syms=t, parent=parent)
        vtrace.Notifier.__init__(self)
        self._db = db
        self._db.registerNotifier(vtrace.NOTIFY_ALL, self)
        for rname in db.canvas.getRendererNames():
            self.mem_canvas.addRenderer(rname, db.canvas.getRenderer(rname))

        self.loadRendSelect()

        if not t.isAttached():
            self.setEnabled(False)
        elif t.isRunning():
            self.setEnabled(False)
        else:
            self._renderMemory()

    @vq_main.idlethreadsync
    def notify(self, event, trace):
        if event in [vtrace.NOTIFY_CONTINUE, vtrace.NOTIFY_DETACH, vtrace.NOTIFY_EXIT]:
            self.setEnabled(False)

        else:
            # If the trace is just going to run again, skip the update.
            if not trace.shouldRunAgain():
                self.setEnabled(True)
                self._renderMemory()

class VdbWindow(vq_app.VQMainCmdWindow, vtrace.Notifier):

    @QtCore.pyqtSlot(int)
    def vqThreadSelected(self, tid):  
        print 'THREAD SELECTED!', tid

    def __init__(self, db):
        vtrace.Notifier.__init__(self)
        # Gui constructor needs these set...
        self._db = db
        self._db_t = vdb.VdbTrace(db)
        self._db.registerNotifier(vtrace.NOTIFY_ALL, self)

        vq_app.VQMainCmdWindow.__init__(self, 'Vdb', db)

        tbar = vtrace_qt.VQTraceToolBar(self._db_t, parent=self)
        self.addToolBar(QtCore.Qt.TopToolBarArea, tbar)

        self.vqAddMenuField('&File.&Quit', self.menuFileQuit)
        self.vqAddMenuField('&View.&Memory', self.menuViewMemory)
        self.vqAddMenuField('&View.&Memory Maps', self.menuViewMemMaps)
        self.vqAddMenuField('&View.&Threads', self.menuViewThreads)
        self.vqAddMenuField('&View.&Registers', self.menuViewRegisters)
        self.vqAddMenuField('&View.&File Descriptors', self.menuViewFileDesc)
        self.vqAddMenuField('&View.&Layouts.&Load', self.menuViewLayoutsLoad)
        self.vqAddMenuField('&View.&Layouts.&Save', self.menuViewLayoutsSave)
        self.vqAddMenuField('&View.&Layouts.&Clear', self.menuViewLayoutsClear)
        self.vqAddMenuField('&Tools.&Python', self.menuToolsPython)

    def vqInitDockWidgetClasses(self):
        self.vqAddDockWidgetClass(VdbMemoryWindow, args=(self._db, self))
        self.vqAddDockWidgetClass(vtrace_qt.VQMemoryMapView, args=(self._db_t, self))
        self.vqAddDockWidgetClass(vtrace_qt.VQFileDescView, args=(self._db_t, self))
        self.vqAddDockWidgetClass(vtrace_qt.VQThreadsView, args=(self._db_t, self, self.vqThreadSelected))
        self.vqAddDockWidgetClass(vtrace_qt.VQRegistersView, args=(self._db_t, self))
        self.vqAddDockWidgetClass(vq_python.VQPythonView, args=(self._db.getExpressionLocals(),))

    def menuToolsPython(self):
        self.vqBuildDockWidget('VQPythonView')

    def menuViewFileDesc(self):
        self.vqBuildDockWidget('VQFileDescView')

    def menuViewMemMaps(self):
        self.vqBuildDockWidget('VQMemoryMapView')

    def menuViewMemory(self):
        self.vqBuildDockWidget('VdbMemoryWindow', floating=True)

    def menuViewThreads(self):
        self.vqBuildDockWidget('VQThreadsView', area=QtCore.Qt.RightDockWidgetArea)

    def menuViewRegisters(self):
        self.vqBuildDockWidget('VQRegistersView', area=QtCore.Qt.RightDockWidgetArea)

    def menuViewLayoutsLoad(self):
        fname = QtGui.QFileDialog.getOpenFileName(self, 'Load Layout')
        if fname == None:
            return

        self.vqClearDockWidgets()

        settings = QtCore.QSettings(fname, QtCore.QSettings.IniFormat)
        self.vqRestoreGuiSettings(settings)

    def menuViewLayoutsSave(self):
        fname = QtGui.QFileDialog.getSaveFileName(self, 'Save Layout')
        if fname == None:
            return

        settings = QtCore.QSettings(fname, QtCore.QSettings.IniFormat)
        self.vqSaveGuiSettings(settings)

    def menuViewLayoutsClear(self):
        self.vqClearDockWidgets()

    def menuFileQuit(self, *args, **kwargs):
        self.close()

    def notify(self, event, trace):
        pass

    def closeEvent(self, event):
        try:
            if self._db.trace.isAttached():
                self._db.trace.detach()
        except Exception, e:
            print('Error Detaching: %s' % e)

        return vq_app.VQMainCmdWindow.closeEvent(self, event)
