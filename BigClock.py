import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog
from BigClockDialog import Ui_bigClockDialog

class BigClock(QDialog, Ui_bigClockDialog):
    
    parent = None
    bigClockDialog = None
    
    def __init__(self, parent=None, name=None):
        super(BigClock, self).__init__(parent)
        self.parent = parent
        
    def showBigClockDialog(self):
        if (self.bigClockDialog is None):
            self.bigClockDialog = QDialog(self.parent,
            QtCore.Qt.WindowTitleHint|QtCore.Qt.WindowCloseButtonHint)
            ui = Ui_bigClockDialog()
            ui.setupUi(self.bigClockDialog)
        ph = self.parent.geometry().height()
        pw = self.parent.geometry().width()
        px = self.parent.geometry().x()
        py = self.parent.geometry().y()
        dw = self.bigClockDialog.width()
        dh = self.bigClockDialog.height()
        # this is how we center the list dialog relative to the main window
        self.bigClockDialog.setGeometry(px-dw-5, py-((dh-ph)/2), dw, dh)
        self.bigClockDialog.show()