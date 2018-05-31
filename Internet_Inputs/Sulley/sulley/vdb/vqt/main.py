import sys
from Queue import Queue
from threading import currentThread

from PyQt4 import QtCore, QtGui

def idlethread(func):
    '''
    A decorator which causes the function to be called by the qt
    main thread rather than synchronously...

    NOTE: This makes the call async handled by the qt main
    loop code.  you can NOT return anything.
    '''
    def idleadd(*args, **kwargs):
        if currentThread().getName() == 'QtThread':
            return func(*args, **kwargs)

        return qapp.proxyOneCall(func, *args, **kwargs)

    return idleadd

def idlethreadsync(func):
    '''
    Similar to idlethread except that it is synchronous and able
    to return values.
    '''
    q = Queue()
    def dowork(*args, **kwargs):
        try:
            q.put(func(*args, **kwargs))
        except Exception, e:
            q.put(e)

    def idleadd(*args, **kwargs):
        if currentThread().getName() == 'QtThread':
            return func(*args, **kwargs)
        qapp.proxyOneCall(dowork, *args, **kwargs)
        return q.get()

    return idleadd

class VQApplication(QtGui.QApplication):

    proxyCall = QtCore.pyqtSignal(name='proxyCall')

    def __init__(self, *args, **kwargs):
        QtGui.QApplication.__init__(self, *args, **kwargs)
        self.proxyCall.connect(self._proxyCaller)
        self.call_proxy_queue = Queue()

    def _proxyCaller(self):
        callable, args, kwargs = self.call_proxy_queue.get()
        return callable(*args, **kwargs)

    def proxyOneCall(self, callable, *args, **kwargs):
        self.call_proxy_queue.put((callable,args,kwargs))
        self.proxyCall.emit()

def startup(css=None):
    global qapp
    qapp = VQApplication(sys.argv)
    if css:
        qapp.setStyleSheet( css )

def main():
    global qapp
    currentThread().setName('QtThread')
    sys.exit(qapp.exec_())

def eatevents():
    qapp.processEvents()

