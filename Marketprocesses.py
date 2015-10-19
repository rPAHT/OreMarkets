__author__ = 'Grant Colasurdo'

import sqlite3
conn = sqlite3.connect('Market.db')
c = conn.cursor()

def CalculateMargin(ItemID, MarketID, Pilot):
    '''
    Ok so first we have to lookup the buy and sell prices of the item at that market
    somehting to the effect of:
    buy = SELECT MIN(Ask) FROM MarketDB WITH ID = ItemID and StationID = MarketID
    sell = SELECT MAX(bid) FROM MarketDB WITH ID = ItemID and StationID = MarketID
    '''
    buyprice = 0
    sellprice = 0



def calcbrokerfee(Pilot, MarketID):
    '''
    :param Pilot: This should be a Pilot object that describes the pilot being used
    this simulation
    :param MarketID: This should be the station that the transaction will be happening
    :return: this should return a constant that represents the multiplier to attach to the
    market order
    '''
    BrokerRelationsSkillLevel = Pilot.sk.BrokerSkillLevel
    BrokerFaction = FactionLookup(MarketID)
    FactionStanding = Pilot.LookupStanding(BrokerFaction)
    PilotCorp = CorpLookup(Pilot)
    CorporationStanding = PilotCorp.LookupStanding(BrokerFaction)

    BF = (.01 - .0005*BrokerRelationsSkillLevel)/ 2^(.1400*FactionStanding+.06000*CorporationStanding)
    if BF <100:
        BF = 100
    return BF



def CalcTax(Pilot):
    Tax = .015*(.1*Pilot.sk.Accounting)
    return Tax

def corplookup(Pilot):
    '''
    :param Pilot: The Pilot Object that is being used for the simulation
    :return: Returns either the Corp Name or something else I don't know yet
    '''
    return Pilot.Corp

def factionlookup(marketID):
    '''
    :param MarketID:This is the ID of the station we are trying to lookup from the DB
    :return:

    We need something to the effect of SELECT Faction FROM StationTable with StationID = MarketID
    '''
    tmp = c.execute("SELECT faction from StationList WHERE stationid=?", marketID)
    if len(tmp) == 1:
        return tmp
    else:
        raise Exception('Station not found from MarketID provided')

