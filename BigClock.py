import sys
from PyQt5 import QtCore
from PyQt5.QtGui import QFont, QFontMetrics
from PyQt5.QtWidgets import QDialog
from BigClockDialog import Ui_bigClockDialog

class BigClock(QDialog, Ui_bigClockDialog):
    
    parent = None
    bigClockDialog = None
    ui = None
    
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
        # this is how we center the list dialog relative to the main window
        self.bigClockDialog.setGeometry(px-dw-5, py-((dh-ph)/2), dw, dh)
        self.bigClockDialog.show()
        
    ''' For setting up a dialog interface for the first time '''
    def setupDialog(self):
        self.bigClockDialog = QDialog(self.parent,
        QtCore.Qt.WindowTitleHint|QtCore.Qt.WindowCloseButtonHint)
        self.ui = Ui_bigClockDialog()
        self.ui.setupUi(self.bigClockDialog)
        self.bigClockDialog.resizeEvent = self.resizeEvent
        # need to set pixel size same as point size, so that resizeEvent() works ok initialy
        # Qt Designer only allows setting font size in points
        f = self.ui.nextRunnerLabel.font()
        f.setPixelSize(f.pointSize())
        self.ui.nextRunnerLabel.setFont(f)
        self.ui.currRunnerLabel.setFont(f)
        f = self.ui.timerLabel.font()
        f.setPixelSize(f.pointSize())
        self.ui.timerLabel.setFont(f)
    
    ''' This event adjusts the label font sizes whenever a dialog is resized '''
    def resizeEvent(self, event):
        dw = event.size().width() - event.oldSize().width()   # width change
        dh = event.size().height() - event.oldSize().height() # height change
        self.resizeLabel(self.ui.nextRunnerLabel, dw, dh)
        self.resizeLabel(self.ui.currRunnerLabel, dw, dh)
        self.resizeLabel(self.ui.timerLabel, dw, dh)
        
    ''' Worker function that does the actual font resizing on a given label '''
    def resizeLabel(self, label, dw, dh):
        # fetch current parameters
        f = label.font()
        cr = label.contentsRect()
        fs = max(f.pixelSize(), 1)
        while True:
            f.setPixelSize(fs)
            br =  QFontMetrics(f).boundingRect(label.text())
            if ((dw >= 0) and (dh >= 0)): # label is expanding
                if ((br.height() <= cr.height()) and (br.width() <= cr.width())):
                    fs += 1
                else:
                    f.setPixelSize(max(fs - 1, 1)) # backtrack
                    break
            else: # label is shrinking
                if ((br.height() > cr.height()) or (br.width() > cr.width())):
                    fs -= 1
                else:
                    break
            if (fs < 1): break
        # update font size
        label.setFont(f)