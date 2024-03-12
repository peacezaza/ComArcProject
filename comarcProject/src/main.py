import math

class HDD:
    writeSpeed = 500
    readSpeed = 500
    def __init__(self,name,capacity):
        self.name = name
        self.capacity = capacity
    def changeCapacity(self,capacity):
        self.capacity = capacity
    def changeName(self,name):
        self.name = name
    def getCapacity(self):
        return self.capacity
    def getName(self):
        return self.name
    def getWriteSpeed(self):
        return self.writeSpeed
    def getReadSpeed(self):
        return self.readSpeed

class RAID:
    def __init__(self,name,level):
        self.RAID_LS = []
        self.name = name
        self.level = level

    def __int__(self):
        return int(self.level)
    def getLevel(self):
        return self.level
    def getName(self):
        return self.name
    def addHDD(self,HDD):
        self.RAID_LS.append(HDD)
    def getRAIDLS(self):
        return self.RAID_LS
    def readSpeed(self):
        if(self.level == 0):
           return len(self.RAID_LS)
        elif(self.level == 1):
           return len(self.RAID_LS)
        elif(self.level == 2):
           pass
        elif(self.level == 3):
            pass
        elif(self.level == 4):
            pass
        elif(self.level == 5):
            return len(self.RAID_LS)-1
        elif(self.level == 6):
            return len(self.RAID_LS)-2
        elif(self.level == 10):
           return len(self.RAID_LS)
    def writeSpeed(self):
        if(self.level == 0):
           return len(self.RAID_LS)
        elif(self.level == 1):
           return 1
        elif(self.level == 2):
           pass
        elif(self.level == 3):
            pass
        elif(self.level == 4):
            pass
        elif(self.level == 5):
            return 1
        elif(self.level == 6):
            return 1
        elif(self.level == 10):
           return int(len(self.RAID_LS)/2)
    def getSUMcapacity(self):
        sum = 0
        min = 100000000
        for i in self.RAID_LS:
            if(i.getCapacity() < min):
                min = i.getCapacity()
        if(self.level == 0):
            if len(self.RAID_LS) >= 2:
                for i in self.RAID_LS:
                    sum += i.getCapacity()
                return sum
            else:
                return "RAID 0 Need 2 driver"
        elif(self.level == 1):
            if len(self.RAID_LS) >= 2:
                return int(((len(self.RAID_LS)/2)*min))
            else:
                return "RAID 1 Need 2 driver"
        elif(self.level == 2):
            if len(self.RAID_LS) >= 3:
                return int(pow(2,math.log2(len(self.RAID_LS)+1)) - math.log2(len(self.RAID_LS)+1) -1 )
            else:
                return "RAID 2 Need 2 driver"
        elif(self.level == 3):
            if len(self.RAID_LS) >= 3:
                return ((len(self.RAID_LS)-1)*min)
            else:
                return "RAID 3 Need 3 driver"
        elif(self.level == 4):
            if len(self.RAID_LS) >= 3:
                return ((len(self.RAID_LS)-1)*min)      
            else:
                return "RAID 4 Need 3 driver"      
        elif(self.level == 5):
            if len(self.RAID_LS) >= 3:
                return ((len(self.RAID_LS)-1)*min)      
            else:
                return "RAID 5 Need 3 driver"      
        elif(self.level == 6):
            if len(self.RAID_LS) >= 4:
                return ((len(self.RAID_LS)-2)*min)
            else:
                return "RAID 6 Need 4 driver"
        elif(self.level == 10):
            if len(self.RAID_LS) >= 4:
                return int((len(self.RAID_LS)/2)*min)
            else:
                return "RAID 10 Need 4 driver"

    



    