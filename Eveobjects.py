__author__ = 'Grant Colasurdo'

import sqlite3

conn = sqlite3.connect('static.db')
c = conn.cursor()

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
        #he we do lookups of the different ores
