'''
A place for some no-brainer basics :)
'''

from PyQt4 import QtCore, QtGui

class VBox( QtGui.QVBoxLayout ):

    def __init__(self, *widgets):
        QtGui.QVBoxLayout.__init__(self)
        self.setMargin(2)
        self.setSpacing(4)
        for w in widgets:
            if w == None:
                self.addStretch()
                continue
            self.addWidget( w )

class HBox( QtGui.QHBoxLayout ):

    def __init__(self, *widgets):
        QtGui.QHBoxLayout.__init__(self)
        self.setMargin(2)
        self.setSpacing(4)
        for w in widgets:
            if w == None:
                self.addStretch()
                continue
            self.addWidget( w )

class ACT:
    def __init__(self, meth, *args, **kwargs):
        self.meth = meth
        self.args = args
        self.kwargs = kwargs

    def __call__(self):
        return self.meth( *self.args, **self.kwargs )

