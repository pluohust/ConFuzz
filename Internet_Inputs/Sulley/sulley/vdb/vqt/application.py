import os
from PyQt4 import QtCore, QtGui

import vqt.cli as vq_cli
import vqt.main as vq_main
import vqt.menubuilder as vq_menu

class VQDockWidget(QtGui.QDockWidget):

    def __init__(self, parent):
        QtGui.QDockWidget.__init__(self, parent)
        self._vq_visible = False
        self.visibilityChanged.connect( self.vqSetVisible )
        #self.connect(self,  QtCore.SIGNAL('visibilityChanged(bool)'), self.vqSetVisible)
        self.setAllowedAreas(QtCore.Qt.AllDockWidgetAreas)

    def vqIsVisible(self):
        return self._vq_visible

    def vqSetVisible(self, visible):
        self._vq_visible = visible

    def vqSaveState(self):
        wid = self.widget()
        if isinstance(wid, VQSavableWidget):
            return wid.vqSaveState()

    def setWidget(self, widget):
        # If he sets his window title, we want to...
        self.setWindowTitle(widget.windowTitle())
        widget.setWindowTitle = self.setWindowTitle
        QtGui.QDockWidget.setWidget(self, widget)

    def vqRestoreState(self):
        pass

    def closeEvent(self, event):
        self.parentWidget().vqRemoveDockWidget(self)
        return QtGui.QDockWidget.closeEvent(self, event)


class VQMainCmdWindow(QtGui.QMainWindow):
    '''
    A base class for application window's to inherit from.
    '''

    def __init__(self, appname, cmd):

        QtGui.QMainWindow.__init__(self)
        self._vq_appname = appname

        self._vq_settings = QtCore.QSettings('invisigoth', application=appname, parent=self)

        self._vq_histfile = os.path.join( os.path.expanduser('~'), '.%s_history' % appname)

        self._dock_widgets = []
        self._dock_classes = {}

        self.vqInitDockWidgetClasses()

        self._vq_mbar = vq_menu.VQMenuBar()
        self.setMenuBar(self._vq_mbar)

        # AnimatedDocks, AllowNestedDocks, AllowTabbedDocks, ForceTabbedDocks, VerticalTabs
        self.setDockOptions(self.AnimatedDocks | self.AllowTabbedDocks)

        self._vq_cli = vq_cli.VQCli(cmd)
        self._vq_cli.loadHistory(self._vq_histfile)
        self._vq_cli.sigCliQuit.connect( self.close )

        self.setCentralWidget(self._vq_cli)
        self.vqRestoreGuiSettings(self._vq_settings)

    def vqAddMenuField(self, fname, callback, args=()):
        self._vq_mbar.addField(fname, callback, args=args)

    def vqAddDynMenu(self, fname, callback):
        self._vq_mbar.addDynMenu(fname, callback)

    def vqInitDockWidgetClasses(self):
        # apps can over-ride
        pass

    def vqAddDockWidgetClass(self, cls, args=()):
        self._dock_classes[cls.__name__] = (cls,args)

    def vqBuildDockWidget(self, clsname, floating=False, area=QtCore.Qt.TopDockWidgetArea):
        res = self._dock_classes.get(clsname)
        if res == None:
            print 'vqBuildDockWidget Failed For: %s' % clsname
            return
        cls, args = res
        obj = cls(*args)
        return self.vqDockWidget(obj, area, floating=floating)

    def vqRestoreGuiSettings(self, settings):

        dwcls = settings.value('DockClasses')
        if not dwcls.isNull():

            for i,clsname in enumerate(dwcls.toStringList()):
                d = self.vqBuildDockWidget(str(clsname), floating=True)
                if d != None:
                    d.setObjectName('VQDockWidget%d' % i)

        # Once dock widgets are loaded, we can restoreState
        state = settings.value('DockState')
        if not state.isNull():
            self.restoreState(state.toByteArray())

        geom = settings.value('DockGeometry')
        if not geom.isNull():
            self.restoreGeometry(geom.toByteArray())

        # Just get all the resize activities done...
        vq_main.eatevents()

        for w in self._dock_widgets:
            w.show()

        return True

    def vqSaveGuiSettings(self, settings):

        dock_classes = []

        # Enumerate the current dock windows and set
        # their names by their list order...
        for i,w in enumerate(self._dock_widgets):

            dock_classes.append(w.widget().__class__.__name__)
            name = 'VQDockWidget%d' % i
            w.setObjectName(name)

        settings.setValue('DockClasses', dock_classes)
        settings.setValue('DockGeometry', self.saveGeometry())
        settings.setValue('DockState', self.saveState())


    def closeEvent(self, event):

        self.vqSaveGuiSettings(self._vq_settings)
        self._vq_cli.saveHistory(self._vq_histfile)
        QtGui.QMainWindow.closeEvent(self, event)

    def vqRemoveDockWidget(self, widget):
        self._dock_widgets.remove(widget)

    def vqClearDockWidgets(self):
        for wid in self._dock_widgets:
            wid.close()

    def vqDockWidget(self, widget, area=QtCore.Qt.TopDockWidgetArea, floating=False):
        d = VQDockWidget(self)
        d.setWidget(widget)
        d.setFloating(floating)
        self.addDockWidget(area, d)
        self._dock_widgets.append(d)
        self.restoreDockWidget(d)
        d.show()
        return d
