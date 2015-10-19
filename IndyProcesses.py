__author__ = 'Grant Colasurdo'

'''
Here we list the many processes that objects can go though in their way thoguh the industrial
chain

We have refining, research, invention, manufacturing and
'''

import sqlite3
conn = sqlite3.connect('indy.db')
c = conn.cursor()

def yld(self, pilot, item, station):
    """
    Here we calcualte the yild of a Indy process given the pilot skill, the item
    and the station that the refining will be taking place at
    :param pilot: The pilot object. this will be used to define the skill levels and
    corp standing
    :param item: this is the item that will be being refined in the case that an ore
    object is passed, we should be able to figure out the quality of the ore in addition
    to the refined amounds
    :param station: this is the station that our simulation will take place in.
    It is used to figure out the station tax as well as the base %yeild that the
    refinery ... yeilds
    :return: a dictionary? I don't know yet but I need it to pass back Item ID numbers and
    quantity numbers for each ID number TBD
    """
    pass


def stationlookup(stationid):
    c.execute('')

