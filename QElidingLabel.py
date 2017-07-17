from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QFontMetrics

'''
    This is a subclass of QLabel to add an additional method
    which elides (adds ... to the right of a string if it's
    too long to fit in a single line).
    This is meant to be added within the Qt Designer, by
    promoting your label with these settings:
        Base class name: QLabel
        Promoted class name: QElidingLabel
        Header file: QElidingLabel
        Global include: unchecked
    This way QElidingLabel is always set when UI is compiled.
    
    NOTICE:
        There are some problems. This elides a text that
        doesn't fit into a single line, even if label is high
        enough to fit the text on two lines.
'''

class QElidingLabel(QtWidgets.QLabel):
    def setElidedText(self, text):
        metrics = QFontMetrics(self.font())
        elided = metrics.elidedText(text, QtCore.Qt.ElideRight, self.width())
        self.setText(elided)
        