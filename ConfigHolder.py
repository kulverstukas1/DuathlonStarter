import os.path
from configparser import ConfigParser

class ConfigHolder:

    #=====================================================
    CONFIG_FILE = "config.ini"
    DEFAULT_SECTION = "MAIN"
    DEFAULTS = {
        "sound_file": ("sound_file", "sounds/quack.wav"),
        "secs_before_first": ("secs_before_first", "5")
    }
    configs = None
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
            configs.write(open(self.CONFIG_FILE, "w"))
    
#=========================================================
    def getSoundFileName(self):
        return self.configs.get(self.DEFAULT_SECTION,
            self.DEFAULTS["sound_file"][0],
            fallback = self.DEFAULTS["sound_file"][1])
#=========================================================
    def getSecsBeforeFirst(self):
        return self.configs.get(self.DEFAULT_SECTION,
            self.DEFAULTS["secs_before_first"][0],
            fallback = self.DEFAULTS["secs_before_first"][1])
#=========================================================