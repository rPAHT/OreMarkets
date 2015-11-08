import numpy as np
import sqlite3 as sql
__author__ = 'rPAHT'


class Pilot:
    def __init__(self, skills, char_id):
        self.sk = skills
        self.id = char_id


class Skill:
    def __init__(
            self, primary_attribute, secondary_attribute,
            training_time_multiplier, required_skills=None
    ):
        self.primary_attribute = primary_attribute
        self.secondary_attribute = secondary_attribute
        self.training_time_multiplier = training_time_multiplier
        if required_skills is None:
            required_skills = []
        self.required_skills = required_skills


class Item:
    def __init__(self, id_num):
        self.id = id_num

    def sql_lookup_connector(self):
        """

        :return: the connector to the sqlite db pointed at the item
        """
        self.c = sql.connect('items.db')


class Ship(Item):
    def __init__(self, id_num):
        Item.__init__(self, id_num)


class Module(Item):
    def __init__(self, id_num):
        Item.__init__(self, id_num)


class Corporation:
    def __init__(
            self, corp_id, corp_name=None, corp_ticker=None, corp_alliance=None,
            corp_ceo=None, corp_member_list=None, corp_url=None, corp_tax_rate=None
    ):
        self.corp_id = corp_id
        self.corp_name = corp_name
        self.ticker = corp_ticker
        self.alliance = corp_alliance
        self.ceo = corp_ceo
        if corp_member_list is None:
            corp_member_list = []
        self.member_list = corp_member_list
        self.url = corp_url
        self.tax_rate = corp_tax_rate


class Alliance:
    def __init__(self, alliance_name, alliance_ticker):
        self.alliance_name = alliance_name
        self.alliance_ticker = alliance_ticker
        self.alliance_members = []

    def add_corp(self, corp):
        self.alliance_members.append(corp)

    def remove_corp(self, corp):
        self.alliance_members.remove(corp)


class Ore(Item):
    def __init__(self, id_num):
        Item.__init__(self, id_num)
        # here we do lookups of the different ores


class Blueprint(Item):
    def __init__(
            self, id_num, item_rank=None, mat_eff=0, time_eff=0,  prod_id=None,
            prod_skill_req=None, prod_base_time=None, prod_mat_reqs=None
    ):
        Item.__init__(self, id_num)
        # What item are we dealing with?
        self.item_rank = item_rank
        # How upgraded is the BP?
        self.mat_eff = mat_eff
        self.time_eff = time_eff
        # How long does it take to upgrade?
        # What can we make with it? and how do we make it?
        self.prod_id = prod_id
        if prod_skill_req is None:
            prod_skill_req = []
        self.prod_skill_req = prod_skill_req
        self.prod_base_time = prod_base_time
        if prod_mat_reqs is None:
            prod_mat_reqs = []
        self.prod_mat_reqs = prod_mat_reqs
        # What are the details on the copy?
        pass
        # here we lookup the blueprint to find all the stuff that defines it


class BPO(Blueprint):
    def __init__(
            self, id_num, mat_eff_time=None, time_eff_time=0, item_rank=None, mat_eff=0, time_eff=0,
            prod_id=None, prod_skill_req=None, prod_base_time=None, prod_mat_reqs=None
    ):
        Blueprint.__init__(
            id_num, item_rank,  mat_eff, time_eff, prod_id, prod_skill_req, prod_base_time, prod_mat_reqs
        )
        self.mat_eff_time = mat_eff_time
        self.time_eff_time = time_eff_time

    def research_mat_efficiency(self):
            if 0 <= self.mat_eff < 10:
                time = np.exp(self.mat_eff+5.37, 2.37869) * self.item_rank
                self.mat_eff += 1
                return time

    def research_time_efficiency(self):
        if 0 <= self.time_eff < 10:
            time = np.exp(self.mat_eff+5.37, 237869)*self.item_rank
            self.mat_eff += 1
            return time


class BPC(Blueprint):
    def __init__(
            self, id_num, item_rank=None, mat_eff=0, time_eff=0, prod_id=None,
            prod_skill_req=None, prod_base_time=None, prod_mat_reqs=None,
            base_copy_time=None, max_runs=None, runs_left=None, base_success=None,
            base_invent_time=None, invent_skill_reqs=None, invent_mat_reqs=None,
            invent_options=None
    ):
        Blueprint.__init__(
            id_num, item_rank, mat_eff, time_eff, prod_id, prod_skill_req, prod_base_time,
            prod_mat_reqs
        )
        self.base_copy_time = base_copy_time
        self.max_runs = max_runs
        self.runs_left = runs_left
        # Invention details
        self.base_success = base_success
        self.base_invent_time = base_invent_time
        self.invent_skill_req = invent_skill_reqs
        self.invent_mat_reqs = invent_mat_reqs
        self.invent_options = invent_options
        pass
