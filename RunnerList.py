import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QAbstractItemView
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QBrush, QColor
from RunnerListDialog import Ui_runnerListDialog

class RunnerList(QDialog, Ui_runnerListDialog):

    parent = None
    runnerListDialog = None
    runnerList = None
    greenBrush = None
    redBrush = None

    def __init__(self, parent=None, name=None):
        super(RunnerList, self).__init__(parent)
        self.parent = parent
        
    ''' Called when we need to show this dialog '''
    def showRunnerListDialog(self, data, currRunner):
        self.reset(data, currRunner)
        self.runnerListDialog.show()
        
    ''' Resets the interface in case new data was loaded '''
    def reset(self, data, currRunner):
        # don't create multiple references, only allow one dialog at a time
        if (self.runnerListDialog is None):
            self.runnerListDialog = QDialog(self.parent,
                QtCore.Qt.WindowTitleHint|QtCore.Qt.WindowCloseButtonHint)
            ui = Ui_runnerListDialog()
            ui.setupUi(self.runnerListDialog)
            self.runnerList = ui.runnerList
            self.runnerList.setSelectionBehavior(QAbstractItemView.SelectRows)
            # self.runnerList.setEnabled(False)
            self.greenBrush = QBrush(QtCore.Qt.green)
            self.redBrush = QBrush(QtCore.Qt.red)
        self.prepRunnerList(self.runnerList, data, currRunner)
    
    ''' Prepares as list of runners with loaded data '''
    def prepRunnerList(self, listObj, data, currRunner):
        headers = ['Bėgikas', 'Laikas', 'Paleistas']
        listModel = QStandardItemModel(0, len(headers))
        listModel.setHorizontalHeaderLabels(headers)
        for index, item in enumerate(data):
            runnerItem = QStandardItem(item["runnerNr"])
            runnerItem.setEditable(False)
            timeItem = QStandardItem(item["time"])
            timeItem.setEditable(False)
            colorItem = QStandardItem("")
            colorItem.setEditable(False)
            if (currRunner-1 > index):
                colorItem.setBackground(self.greenBrush)
            else:
                colorItem.setBackground(self.redBrush)
            listModel.appendRow([runnerItem, timeItem, colorItem])
        listObj.setModel(listModel)
    
    ''' Resets the last column color to red for all runners '''
    def resetColor(self):
        listModel = self.runnerList.model()
        rowCount = listModel.rowCount()
        for i in range(rowCount):
            item = listModel.item(i, 2)
            item.setBackground(self.redBrush)
            listModel.setItem(i, 2, item)
    
    ''' Marks the runner green when he is to go '''
    def markGreen(self, runner):
        # this is to compensate for the first runner
        if (runner > 0):
            runner -= 1
            listModel = self.runnerList.model()
            item = listModel.item(runner, 2)
            item.setBackground(self.greenBrush)
            listModel.setItem(runner, 2, item)