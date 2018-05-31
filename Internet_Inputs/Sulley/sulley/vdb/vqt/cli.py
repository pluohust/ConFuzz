import os
from PyQt4 import QtCore, QtGui

import envi.cli as e_cli
import envi.qt.memory as e_q_memory
import envi.qt.memcanvas as e_q_memcanvas

from envi.threads import firethread

import vqt.colors as vq_colors
import vqt.shortcut as vq_shortcut

from vqt.basics import *
from vqt.main import idlethread

class VQCli(QtGui.QWidget):
    '''
    A Qt class to wrap and emulate a Cmd object.
    '''

    __canvas_class__ = e_q_memcanvas.VQMemoryCanvas

    sigCliQuit = QtCore.pyqtSignal()

    def __init__(self, cli, parent=None):
        QtGui.QWidget.__init__(self, parent=parent)
        self.cli = cli

        self.input = QtGui.QLineEdit(self)

        # Create our output window...
        self.output = QtGui.QTextEdit(self)
        # If it's an EnviCli, let's over-ride the canvas right away.
        if isinstance(cli, e_cli.EnviCli):
            self.output.close()
            self.output = self.__canvas_class__(cli.memobj, syms=cli.symobj, parent=self)
            self.output.setScrolledCanvas(True)
            cli.setCanvas(self.output)

        self.setStyleSheet( vq_colors.getDefaultColors() )

        # Create they vertical layout and add widgets...
        vbox = VBox( self.output, self.input )
        self.setLayout(vbox)

        self.connect(self.input,  QtCore.SIGNAL('returnPressed()'), self.returnPressedSlot)

        vq_shortcut.addShortCut(self.input, QtCore.Qt.Key_Up, self.keyCodeUp)
        vq_shortcut.addShortCut(self.input, QtCore.Qt.Key_Down, self.keyCodeDown)

        self.history = []
        self.histidx = 0

        self.resize(250, 150)

    def returnPressedSlot(self):
        cmd = str(self.input.text())
        self.input.clear()
        self.addHistory(cmd)
        self.output.addText('> %s\n' % cmd)
        firethread(self.onecmd)(cmd)

    def onecmd(self, cmdline):
        if self.cli.onecmd( cmdline ):
            self._emit_quit()

    @idlethread
    def _emit_quit(self):
        # A way to emit the "quit" signal from threads other than the
        # qt main thread.
        self.sigCliQuit.emit()

    def useHistory(self, delta):

        if delta < 0 and self.histidx == 0:
            return

        if delta > 0 and len(self.history) <= self.histidx+delta:
            self.histidx = len(self.history)
            self.input.clear()
            return

        self.histidx += delta
        htext = self.history[self.histidx]
        self.input.setText(htext)
        #self.input.selectAll()

    def addHistory(self, histcmd):
        if histcmd:
            self.history.append(histcmd)
            self.histidx = len(self.history)

    def keyCodeUp(self,*args):
        self.useHistory(-1)

    def keyCodeDown(self):
        self.useHistory(1)

    def loadHistory(self, filename):
        if os.path.isfile(filename):
            hist = file(filename, 'r').readlines()[-1000:]
            self.history = [ x.strip() for x in hist ]
            self.histidx = len(self.history)

    def saveHistory(self, filename):
        # Only save the last 1000 commands
        # (gotta put a limit somewhere...)
        histbuf = '\n'.join( self.history[-1000:] )
        file(filename, 'w').write( histbuf )

