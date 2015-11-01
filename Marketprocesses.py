import sqlite3

__author__ = 'rPAHT'

conn = sqlite3.connect('Market.db')
c = conn.cursor()


def calculate_margin(item_ID, market_ID, pilot):
    """
    Ok so first we have to lookup the buy and sell prices of the item at that market
    something to the effect of:
    buy = SELECT MIN(Ask) FROM MarketDB WITH ID = ItemID and StationID = MarketID
    sell = SELECT MAX(bid) FROM MarketDB WITH ID = ItemID and StationID = MarketID
    """
    buyprice = 0
    sellprice = 0


def calc_broker_fee(pilot, station):
    """
    :param pilot: This should be a Pilot object that describes the pilot being used
    this simulation
    :param market_ID: This should be the station that the transaction will be happening
    :return: this should return a constant that represents the multiplier to attach to the
    market order
    """
    broker_relations_skill_level = pilot.sk.BrokerSkillLevel
    broker_faction = station.faction
    faction_standing = pilot.standing_lookup(broker_faction)
    pilot_corp = pilot.corp
    corporation_standing = pilot_corp.standing_lookup(broker_faction)

    broker_fee = (.01 - .0005 * broker_relations_skill_level) / (
                 2 ** (.1400 * faction_standing + .06000 * corporation_standing))
    if broker_fee < 100:
        broker_fee = 100
    return broker_fee


def calc_tax(pilot):
    tax = .015 * (.1 * pilot.skill_level_query("Accounting"))
    return tax


def faction_lookup(market_ID):
    """
    :param market_ID:This is the ID of the station we are trying to lookup from the DB
    :return:

    We need something to the effect of SELECT Faction FROM StationTable with StationID = MarketID
    """
    tmp = c.execute("SELECT faction from StationList WHERE station_id=?", market_ID)
    if len(tmp) == 1:
        return tmp
    else:
        raise Exception('Station not found from MarketID provided')
