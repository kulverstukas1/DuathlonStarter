import re
from datetime import datetime

class DataParser:
    
    #=====================================================
    # Needed for data validation
    DATA_STRUCTURE_REGEX = "^[\d\w\s\.,]+\t\d{1,2}:\d{1,2},\d{1}$";
    # Needed for time validation
    TIME_FORMAT = "%M:%S,%f"
    # Here we hold our loaded runner data
    LOADED_DATA = []
    # Keep a record which runner is current one
    currentRunnerIndex = 0
    #=====================================================
    
    def __init__(self):
        pass

#=========================================================
    '''
        If data is from 2 arays (runner nr. and times are separate)
        then we need to join them before processing
    '''
    def joinRunnerData(self, data):
        if ((type(data) == list) and (len(data) == 2)):
            runnerNrs = data[0].split("\n")
            runnerTimes = data[1].split("\n")
            if (len(runnerNrs) == len(runnerTimes)):
                return "\n".join([runnerNr.strip()+"\t"+runnerTimes[i].strip() for i, runnerNr in enumerate(runnerNrs)])
            else:
                return ""
        else:
            return ""
#=========================================================
    '''
        Data structure verification happens by checking each line with
        regex, if the line doesn't match, then the format is invalid.
    '''
    def verifyDataStructure(self, data):
        compiledRegex = re.compile(self.DATA_STRUCTURE_REGEX)
        for line in data.split("\n"):
            # print(line)
            if (compiledRegex.match(line.strip()) is None):
                return False
        return True
#=========================================================
    ''' Method for loading data into an array for better management '''
    def loadData(self, data):
        self.LOADED_DATA = [] # Clear previous entries
        # we need to make the whole thing unified
        dataLines = []
        for line in data.split("\n"):
            runner, mins, secs, millis = re.split("[\t:,]", line.strip())
            mins = mins.zfill(2)
            secs = secs.zfill(2)
            dataLines.append("%s	%s:%s,%s" % (runner, mins, secs, millis))
        lines = sorted(dataLines, key=self.sortingKey)
        # print(lines)
        prevTimeInMillis = 0
        timeInMillis = 0
        for line in lines:
            runnerNr, time = line.strip().split("\t")
            timeObj = datetime.strptime(time, self.TIME_FORMAT)
            timeInMillis = int(
                (((timeObj.minute*60)+timeObj.second)*1000)+(timeObj.microsecond/1000)
            )
            if (prevTimeInMillis != 0):
                timeDiff = timeInMillis - prevTimeInMillis
            else:
                timeDiff = 0
            # print("%d" % timeDiff)
            self.LOADED_DATA.append({
                "runnerNr":runnerNr,
                "time":time,
                "timeInMillis":timeInMillis,
                "timeDiff":timeDiff})
            prevTimeInMillis = timeInMillis
#=========================================================
    ''' Resets the counters and indexes '''
    def reset(self):
        self.currentRunnerIndex = 0
#=========================================================
    ''' Returns all the data that we have loaded '''
    def getAllData(self):
        return self.LOADED_DATA
#=========================================================
    ''' Gets the next runner on the list, returns false if there's no more runners '''
    def getNextRunner(self):
        if (len(self.LOADED_DATA) > self.currentRunnerIndex+1):
            return self.LOADED_DATA[self.currentRunnerIndex+1]
        return False
#=========================================================
    ''' Gets the current runner on the list, returns false if there's no more runners '''
    def getCurrentRunner(self):
        if (len(self.LOADED_DATA) > self.currentRunnerIndex):
            return self.LOADED_DATA[self.currentRunnerIndex]
        return False
#=========================================================
    ''' Gets the total number of loaded runners '''
    def getTotalRunners(self):
        return len(self.LOADED_DATA)
#=========================================================
    ''' Gets the current runner number in array '''
    def getCurrentRunnerNum(self):
        return self.currentRunnerIndex
#=========================================================
    ''' Set the array index on another runner '''
    def setOnNextRunner(self):
        self.currentRunnerIndex += 1
#=========================================================
    ''' Formats the given milliseconds into a nicer format '''
    def formatMillis(self, millis):
        try:
            # return datetime.fromtimestamp((millis / 1000)).strftime("%M:%S,%f")[:-5]
            (dt, micro) = (datetime.fromtimestamp((millis / 1000)).strftime(self.TIME_FORMAT)).split(',')
            dt = "%s,%03d" % (dt, round(int(micro), -1) / 1000)
            return dt[:-2]
        except:
            return "ER:ER,E"
#=========================================================
    '''
        Function that is used in sorted() to sort out given times.
        This returns the time string as a whole integer without
        symbols and zeroes.
    '''
    def sortingKey(self, s):
        rtn = re.sub("[:,]", "", s.split("\t")[1]).lstrip("0")
        return int(rtn) if rtn != "" else 0
#=========================================================
