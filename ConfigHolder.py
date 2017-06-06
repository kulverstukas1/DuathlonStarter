import os
import math
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from configparser import ConfigParser
from SettingsDialog import Ui_settingsDialog

class ConfigHolder:

    #=====================================================
    CONFIG_FILE = "config.ini"
    DEFAULT_SECTION = "MAIN"
    DEFAULTS = {
        "sound_file": ("sound_file", "sounds/quack.wav"),
        "secs_before_first": ("secs_before_first", "5")
    }
    configs = None
    settingsDialog = None
    #=====================================================
    
    def __init__(self):
        beenChanges = False
        self.configs = ConfigParser()
        if (os.path.isfile(self.CONFIG_FILE)):
            self.configs.read_file(open(self.CONFIG_FILE, "r"))
            for key in self.DEFAULTS:
                if (key not in self.configs.options(self.DEFAULT_SECTION)):
                    self.configs.set(self.DEFAULT_SECTION, key, self.DEFAULTS[key][1])
                    if (not beenChanges): beenChanges = True
        else:
            self.configs.add_section(self.DEFAULT_SECTION)
            for key in self.DEFAULTS:
                self.configs.set(self.DEFAULT_SECTION, key, self.DEFAULTS[key][1])
                if (not beenChanges): beenChanges = True
        
        if (beenChanges):
            self.configs.write(open(self.CONFIG_FILE, "w"))
    
#=========================================================
    def getSoundFileName(self):
        return self.configs.get(self.DEFAULT_SECTION,
            self.DEFAULTS["sound_file"][0],
            fallback = self.DEFAULTS["sound_file"][1])
#=========================================================
    def getSecsBeforeFirst(self):
        return int(self.configs.get(self.DEFAULT_SECTION,
            self.DEFAULTS["secs_before_first"][0],
            fallback = self.DEFAULTS["secs_before_first"][1]))
#=========================================================
    def resetPreStartSecs(self):
        if (not self.configs.get(self.DEFAULT_SECTION,
            self.DEFAULTS["secs_before_first"][0]).isdigit()):
            self.configs.set(self.DEFAULT_SECTION,
                self.DEFAULTS["secs_before_first"][0],
                self.DEFAULTS["secs_before_first"][1])
            self.configs.write(open(self.CONFIG_FILE, "w"))
            return True
        else:
            return False
#=========================================================
    ''' Show a settings dialog to change some preferences '''
    def showSettingsDialog(self, context):
        self.settingsDialog = QtWidgets.QDialog(context,
            QtCore.Qt.WindowTitleHint|QtCore.Qt.WindowCloseButtonHint)
        ui = Ui_settingsDialog()
        ui.setupUi(self.settingsDialog)
        ui.soundFilePath.setText(self.configs.get(self.DEFAULT_SECTION, "sound_file"))
        ui.preStartSecs.setValue(int(self.configs.get(self.DEFAULT_SECTION, "secs_before_first")))
        ui.selectSoundFile.clicked.connect(lambda: selectSoundFileBtnCallback(ui))
        ui.okBtn.clicked.connect(lambda: okBtnClick(self.settingsDialog, ui))
        ui.cancelBtn.clicked.connect(self.settingsDialog.close)
        self.settingsDialog.setFixedSize(self.settingsDialog.size())
        self.settingsDialog.show()
        #---Callbacks---
        def selectSoundFileBtnCallback(ui):
            fileDialog = QFileDialog()
            fileDialog.setFileMode(QFileDialog.ExistingFile)
            fileDialog.setNameFilter("Garso failai (*.wav)")
            if (fileDialog.exec_()):
                ui.soundFilePath.setText(os.path.relpath((fileDialog.selectedFiles()[0])))
        #---------------
        def okBtnClick(settingsDlg, ui):
            self.configs.set(self.DEFAULT_SECTION, "sound_file", ui.soundFilePath.text())
            self.configs.set(self.DEFAULT_SECTION, "secs_before_first", str(ui.preStartSecs.value()))
            self.configs.write(open(self.CONFIG_FILE, "w"))
            settingsDlg.close()
        #---/Callbacks---
#=========================================================