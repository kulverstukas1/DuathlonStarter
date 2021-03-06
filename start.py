import sys
import os
import winsound
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from MainWindow import Ui_MainWindow
from AboutDialog import Ui_aboutDialog
from LoadDataDialog import Ui_fromMemoryDialog
from DataParser import DataParser
from ConfigHolder import ConfigHolder
from RunnerList import RunnerList
from BigClock import BigClock

class Start(QMainWindow, Ui_MainWindow):
    
    #=====================================================
    '''
        We need to keep these references, otherwise they get garbage
        collected really fast
    '''
    aboutDialog = None
    fromMemoryDialog = None
    dataParser = None
    configs = None
    runnerTimer = None
    windowIcon = None
    runnerList = None
    bigClock = None
    # Needed for timekeeping
    currRunnerMillisDiff = 0
    TIMER_FREQUENCY = 10
    #=====================================================

    def __init__(self, parent=None, name=None):
        super(Start, self).__init__(parent)
        self.dataParser = DataParser()
        self.configs = ConfigHolder()
        self.runnerList = RunnerList(self)
        self.bigClock = BigClock(self)
        self.runnerTimer = QtCore.QTimer(self)
        self.runnerTimer.timeout.connect(self.timerTickCallback)
        self.setupUi(self)
        self.setFixedSize(self.size())
        
        self.windowIcon = QtGui.QIcon()
        self.windowIcon.addPixmap(QtGui.QPixmap(self.resource_path("images/program_icon.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        
        self.setWindowIcon(self.windowIcon)
        
        self.action_information.triggered.connect(self.aboutMenuClicked)
        self.action_fromMemory.triggered.connect(self.fromMemoryMenuClicked)
        self.action_fromFile.triggered.connect(self.fromFileMenuClicked)
        self.action_settings.triggered.connect(lambda: self.configs.showSettingsDialog(self))
        self.action_bigTimer.triggered.connect(self.showBigClockDialog)
        self.action_runnerList.triggered.connect(lambda: self.runnerList.showRunnerListDialog(
            self.dataParser.getAllData(),
            self.dataParser.getCurrentRunnerNum()
        ))
        
        self.startBtn.clicked.connect(self.startBtnClicked)
        self.stopBtn.clicked.connect(self.stopBtnClicked)
        self.resetBtn.clicked.connect(self.resetBtnClicked)
            
        self.checkSettings()
            
    ''' Event that fires when we're closing the main window '''
    def closeEvent(self, event):
        # If the timer is running, then ask to confirm
        if (self.runnerTimer.isActive()):
            reply = QMessageBox.question(self,
                "Ar tikrai?",
                "Laikmatis yra aktyvus. Ar tikrai norite išeiti?",
                QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if (reply == QMessageBox.Yes):
                event.accept()
            else:
                event.ignore()
        else:
            event.accept()
#=========================================================
    ''' Callback for a timer ticker '''
    def timerTickCallback(self):
        if (self.currRunnerMillisDiff > 0):
            self.currRunnerMillisDiff -= self.TIMER_FREQUENCY
            millisText = self.dataParser.formatMillis(self.currRunnerMillisDiff)
            self.timerLabel.setText(millisText)
            self.bigClock.updateTimeLabel(millisText)
        else:
            currentRunner = self.dataParser.getCurrentRunner()
            if (self.dataParser.getCurrentRunnerNum() > 0):
                winsound.PlaySound(self.configs.getSoundFileName(), winsound.SND_ASYNC)
                if (currentRunner):
                    self.bigClock.updateRunnerLabels(currentRunner["runnerNr"])
            self.runnerList.markGreen(self.dataParser.getCurrentRunnerNum())
            if (currentRunner):
                if (self.dataParser.getCurrentRunnerNum() == 0):
                    currentRunner["timeDiff"] = self.configs.getSecsBeforeFirst()*1000
                self.currRunnerMillisDiff = currentRunner["timeDiff"]
                self.currentRunnerGroup.setTitle("Bus paleistas: %d iš %d" %
                    (self.dataParser.getCurrentRunnerNum()+1, self.dataParser.getTotalRunners()))
                self.currentRunnerNr.setElidedText("Dalyvis: %s" % currentRunner["runnerNr"])
                self.currentRunnerTime.setText("Laikas: %s" % currentRunner["time"])
                
                nextRunner = self.dataParser.getNextRunner()
                if (not nextRunner): nextRunner = {"runnerNr":"---", "time":"---", "timeInMillis":0}
                self.nextRunnerNr.setElidedText("Dalyvis: %s" % nextRunner["runnerNr"])
                self.nextRunnerTime.setText("Laikas: %s" % nextRunner["time"])
                self.currentDifference.setText(
                    self.dataParser.formatMillis(
                        nextRunner['timeInMillis']-currentRunner["timeInMillis"]
                    ) if (nextRunner['timeInMillis'] > currentRunner["timeInMillis"]) else "---"
                )
                
            else:
                self.runnerTimer.stop()
                self.startBtn.setEnabled(True)
                self.stopBtn.setEnabled(False)
                self.resetBtn.setEnabled(True)
                self.enableMenuBarItems()
                self.bigClock.updateRunnerLabels("---")
            # need to call this here, for RunnerList to work properly
            self.dataParser.setOnNextRunner()
#=========================================================
    ''' Shows information about this program '''
    def aboutMenuClicked(self):
        self.aboutDialog = QtWidgets.QDialog(self,
            QtCore.Qt.WindowTitleHint|QtCore.Qt.WindowCloseButtonHint)
        ui = Ui_aboutDialog()
        ui.setupUi(self.aboutDialog)
        self.aboutDialog.setFixedSize(self.aboutDialog.size())
        self.aboutDialog.show()
        self.aboutDialog = None
    #------------
    ''' Shows a dialog where you can paste your data and load it '''
    def fromMemoryMenuClicked(self):
        self.fromMemoryDialog = QtWidgets.QDialog(self,
            QtCore.Qt.WindowTitleHint|QtCore.Qt.WindowCloseButtonHint)
        ui = Ui_fromMemoryDialog()
        ui.setupUi(self.fromMemoryDialog)
        ui.dataText.setVisible(False)
        ui.runnerNrDataText.setFocus()
        self.fromMemoryDialog.setFixedSize(self.fromMemoryDialog.size())
        ui.clearBtn.clicked.connect(lambda: clearBtnCallback(ui))
        ui.cancelBtn.clicked.connect(self.fromMemoryDialog.close)
        ui.okBtn.clicked.connect(lambda: okBtnCallback(self.fromMemoryDialog, ui))
        ui.inputMethodToggle.stateChanged.connect(lambda: checkBoxCallback(ui))
        self.fromMemoryDialog.show()
        #------------
        def okBtnCallback(dialog, ui):
            if (ui.inputMethodToggle.isChecked()):
                data = ui.dataText.toPlainText().strip()
            else:
                data = self.dataParser.joinRunnerData(
                    [ui.runnerNrDataText.toPlainText().strip(),
                    ui.runnerTimeDataText.toPlainText().strip()])
            if (self.checkData(data, dialog)):
                self.dataParser.loadData(data)
                self.populateGui()
        #------------
        def checkBoxCallback(ui):
            if (ui.inputMethodToggle.isChecked()):
                ui.dataText.setVisible(True)
                ui.dataText.setFocus()
                ui.runnerTimeDataText.clear()
                ui.runnerNrDataText.clear()
                ui.runnerDataFrame.setVisible(False)
            else:
                ui.dataText.clear()
                ui.dataText.setVisible(False)
                ui.runnerDataFrame.setVisible(True)
                ui.runnerNrDataText.setFocus()
        #------------
        def clearBtnCallback(ui):
            if (ui.inputMethodToggle.isChecked()):
                ui.dataText.clear()
            else:
                ui.runnerTimeDataText.clear()
                ui.runnerNrDataText.clear()
    #------------
    ''' Shows a file selection dialog to select the data file and load it '''
    def fromFileMenuClicked(self):
        fileDialog = QFileDialog()
        fileDialog.setFileMode(QFileDialog.ExistingFile)
        fileDialog.setNameFilter("Tekstiniai failai (*.txt)")
        if (fileDialog.exec_()):
            with open(fileDialog.selectedFiles()[0], "r") as f:
                fContents = f.read().strip()
            if (self.checkData(fContents, None)):
                self.dataParser.loadData(fContents)
                self.populateGui()
    #------------
    ''' Starts the countdown and beeps '''
    def startBtnClicked(self):
        currNum = self.dataParser.getCurrentRunnerNum()
        total = self.dataParser.getTotalRunners()
        if (currNum > total): self.populateGui()
        self.startBtn.setEnabled(False)
        self.stopBtn.setEnabled(True)
        self.resetBtn.setEnabled(False)
        self.disableMenuBarItems()
        self.runnerTimer.start(self.TIMER_FREQUENCY)
    #------------
    ''' Stops the timer but doesn't reset anything '''
    def stopBtnClicked(self):
        self.startBtn.setEnabled(True)
        self.stopBtn.setEnabled(False)
        self.resetBtn.setEnabled(True)
        self.runnerTimer.stop()
        self.enableMenuBarItems()
    #------------
    ''' Resets the whole counter as if data was just loaded '''
    def resetBtnClicked(self):
        self.startBtn.setEnabled(True)
        self.stopBtn.setEnabled(False)
        self.resetBtn.setEnabled(True)
        self.dataParser.reset()
        self.runnerList.resetColor()
        self.currRunnerMillisDiff = 0
        self.populateGui()
    #------------
    ''' Shows a big timer clock for everyone to see '''
    def showBigClockDialog(self):
        self.bigClock.showBigClockDialog(self.configs.getBigClockSizeIncrease())
#=========================================================
    ''' Check if loaded settings are correct and show a message if not '''
    def checkSettings(self):
        # if the sound file doesn't exist then show a warning
        msg = QMessageBox()
        msg.setWindowIcon(self.windowIcon)
        msg.addButton(QMessageBox.Ok)
        if (not os.path.isfile(self.configs.getSoundFileName())):
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Klaida")
            msg.setText("Nurodytas garso failas (%s) neegzistuoja." % self.configs.getSoundFileName())
            msg.exec_()
        if (self.configs.resetPreStartSecs()):
            self.configs.resetPreStartSecs()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Įspėjimas")
            msg.setText("Nurodytos sekundės nėra skaičius. Atstatyta į %d." % self.configs.getSecsBeforeFirst())
            msg.exec_()
#=========================================================
    ''' Here we check if the selected/entered data is valid and can be parsed '''
    def checkData(self, data, dialog):
        verified = self.dataParser.verifyDataStructure(data)
        if (verified):
            if (dialog is not None): dialog.close()
        else:
            QMessageBox.critical(self, "Klaida", "Bloga duomenų struktūra.\nTinkama struktūra: Vardas[tab]00:00,0", QMessageBox.Ok)
        return verified
#=========================================================
    ''' Enables needed menu bar items '''
    def enableMenuBarItems(self):
        self.menuData.setEnabled(True)
        self.menuSettings.setEnabled(True)
        self.menuAbout.setEnabled(True)
    #------------
    ''' Disables needed menu bar items '''
    def disableMenuBarItems(self):
        self.menuData.setEnabled(False)
        self.menuSettings.setEnabled(False)
        self.menuAbout.setEnabled(False)
#=========================================================
    ''' Populates the main GUI with data we have loaded and preps DataParser '''
    def populateGui(self):
        self.startBtn.setEnabled(True)
        self.stopBtn.setEnabled(False)
        self.resetBtn.setEnabled(True)
        
        self.currentRunnerGroup.setTitle("Bus paleistas")
        self.currentRunnerNr.setText("Dalyvis:")
        self.currentRunnerTime.setText("Laikas:")
        
        self.timerLabel.setText("00:00,0")
        self.currentDifference.setText("00:00,0")
        # Need to reset the counters in case we're on the last runner
        self.dataParser.reset()
        self.runnerList.reset(self.dataParser.getAllData(), self.dataParser.getCurrentRunnerNum())
        self.currRunnerMillisDiff = 0
        # Data was just loaded, so show the first runner on our list
        currentRunner = self.dataParser.getCurrentRunner()
        self.nextRunnerNr.setElidedText("Dalyvis: %s" % currentRunner["runnerNr"])
        self.nextRunnerTime.setText("Laikas: %s" % currentRunner["time"])
        self.bigClock.updateTimeLabel("00:00,0")
        self.bigClock.resetRunnerLabels()
        self.bigClock.updateRunnerLabels(currentRunner["runnerNr"])
#=========================================================
    ''' Get absolute path to resource, works for dev and for PyInstaller '''
    def resource_path(self, relative_path):
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)
#=========================================================
if __name__ == '__main__':
    app = QApplication(sys.argv)
    startClass = Start()
    startClass.show()
    sys.exit(app.exec_())