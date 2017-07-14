import sys
from PyQt5 import QtCore
from PyQt5.QtGui import QFont, QFontMetrics
from PyQt5.QtWidgets import QDialog
from BigClockDialog import Ui_bigClockDialog

class BigClock(QDialog, Ui_bigClockDialog):
    
    parent = None
    bigClockDialog = None
    ui = None
    runnerInfo = {"current": "---", "next": "---"}
    
    def __init__(self, parent=None, name=None):
        super(BigClock, self).__init__(parent)
        self.parent = parent
        
    ''' Called when a giant-ass clock needs to be shown '''
    def showBigClockDialog(self):
        if (self.bigClockDialog is None):
            self.setupDialog()
        ph = self.parent.geometry().height()
        pw = self.parent.geometry().width()
        px = self.parent.geometry().x()
        py = self.parent.geometry().y()
        dw = self.bigClockDialog.width()
        dh = self.bigClockDialog.height()
        # this is how we center the clock dialog relative to the main window
        self.bigClockDialog.setGeometry(px-dw-5, py-((dh-ph)/2), dw, dh)
        self.bigClockDialog.show()
        
    ''' For setting up a dialog interface for the first time '''
    def setupDialog(self):
        self.bigClockDialog = QDialog(self.parent,
        QtCore.Qt.WindowTitleHint|QtCore.Qt.WindowCloseButtonHint)
        self.ui = Ui_bigClockDialog()
        self.ui.setupUi(self.bigClockDialog)
        self.ui.nextRunnerLabel.setText("")
        self.ui.currRunnerLabel.setText("")
        self.ui.timerLabel.setText("00:00,0")
    
    ''' Updates this dialog with given formatted time '''
    def updateTimeLabel(self, time):
        if (self.ui is not None):
            self.ui.timerLabel.setText(time)
        
    ''' Updates this dialog with runner status. Moves next to current '''
    def updateRunnerLabels(self, runner):
        if (self.ui is not None):
            self.runnerInfo["current"] = self.runnerInfo["next"]
            self.runnerInfo["next"] = runner
            self.ui.currRunnerLabel.setText(self.runnerInfo["current"])
            self.ui.nextRunnerLabel.setText(self.runnerInfo["next"])
        