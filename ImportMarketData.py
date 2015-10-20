__author__ = 'Grant Colasurdo'

import urllib.request
import urllib.parse
import urllib.error
import shutil
import gzip
import mysql.connector
import os


weburl = "http://eve-marketdata.com/developers/"

irregularlist = ["mysql_eve_inv_types.txt.gz", "mysql_eve_map_regions.txt.gz", "mysql_eve_map_solarsystem_jumps.txt.gz",
                 "mysql_eve_map_solarsystems.txt.gz", "mysql_eve_sta_stations.txt.gz"]

nightlylist = ["mysql_eve_inv_types.txt.gz", "mysql_items_buying.txt.gz", "mysql_items_buying_jita.txt.gz",
               "mysql_items_selling.txt.gz", "mysql_items_selling_jita.txt.gz", "mysql_station_rank.txt.gz",
               "mysql_items_history_theforge_90.txt.gz", "mysql_region_type_updates.txt.gz",
               "mysql_region_type_hist_updates.txt.gz"]


dire = "C:\\Users\Grant Colasurdo\PycharmProjects\Eve\OreMarkets\MarketDumps\\"
for dfile in nightlylist:

    url = weburl + dfile
    file_name = dire + dfile
    comp_name = file_name[:file_name.rfind(".")]
    print("downloading " + url[url.rfind("/") + 1:])
    with urllib.request.urlopen(url) as response, open(file_name, 'wb') as out_file, open(comp_name, 'wb') as comp_file:
        print("Unpacking " + file_name + " ...")
        shutil.copyfileobj(response, comp_name)
        unpack = gzip.open(comp_name)
        shutil.copyfileobj(unpack, file_name)


cnx = mysql.connector.connect(user='grant', password='Warhammer',
                              host='127.0.0.1', database='static')
