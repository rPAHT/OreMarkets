__author__ = 'Grant Colasurdo'
import numpy as np

class Item:
    def __init__(self, idnum):
        self.id = idnum


class Pilot:
    def __init__(self, skills, charid):
        self.sk = skills
        self.id = charid
        

class Ship:
    def __init__(self, idnum):
        self.id = idnum


class Module:
    def __init__(self, idnum):
        self.id = idnum


class Corporation:
    def __init__(self, idnum):
        self.id = idnum


class Ore:
    def __init__(self, idnum):
        self.idnum = idnum
        # here we do lookups of the different ores


class Blueprint:
    def __init__(self, idnum):
        # What item are we dealing with?
        self.idnum = idnum
        self.itemrank = None
        # How upgraded is the BP?
        self.mateff = 0
        self.timeeff = 0
        # How long does it take to upgrade?
        self.matefftime = None
        self.timeefftime = None
        # What can we make with it? and how do we make it?
        self.prodid = None
        self.prodskillreq = [None]
        self.prodbasetime = None
        self.prodmatreqs = {}
        # Is this a copy or an original?
        self.copy = False
        # What are the details on the copy?
        self.basecopytime = None
        self.maxruns = 0
        self.runsleft = None
        # Invention details
        self.basesuccess = 0
        self.baseinventtime = None
        self.inventskillreq = [None]
        self.inventmatreqs = {}
        self.inventoptions = [None]
        pass

    def researchmatefficency(self):
            if 0 <= self.mateff < 10:
                time = np.exp(self.mateff+5.37, 2.37869) * self.itemrank
                self.mateff += 1

        # here we lookup the blueprint to find all the stuff that defines it


