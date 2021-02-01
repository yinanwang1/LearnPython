#!/usr/bin/env python
# -*- coding:utf8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import time
import random

_st = 1420041600*1000


def geneId():
    t = time.time()*1000
    return str(t-_st)+"{0:06}".format(random.randint(0, 999999))


def get_session(connstr):
    return get_scoped_session(connstr)()


def get_scoped_session(connstr):
    _engine = create_engine(connstr, pool_recycle=1800)
    _scoped_session = scoped_session(sessionmaker(autoflush=True))
    _scoped_session.configure(bind=_engine)
    return _scoped_session


# session=get_session("mysql+mysqldb://admin:admin@db.59temai.com:3306/db59store_dev?charset=utf8")

class DBHelper(object):
    @classmethod
    def get_insert_sql(cls, struct, obj):
        tname = struct["name"]
        cols = struct["cols"]
        return cls.insert_sql(tname, cols, obj)

    @classmethod
    def get_update_sql(cls, struct, conditions, obj):
        tname = struct["name"]
        cols = struct["cols"]
        return cls.update_sql(tname, cols, conditions, obj)

    @classmethod
    def get_select_sql(cls, struct, conditions):
        tname = struct["name"]
        cols = struct["cols"]
        return cls.select_sql(tname, cols, conditions)

    @classmethod
    def select_sql(cls, tname, col_names, conditions):
        cols = []
        for k in col_names:
            item = "`{0}`".format(k)
            cols.append(item)

        wheres = ["1=1"]
        for k in conditions:
            item = "`{0}`=:{0}".format(k)
            wheres.append(item)
        fmt = """ select {0} from {1} where {2} """
        return fmt.format(",".join(cols) or "*", tname, " and ".join(wheres))

    @classmethod
    def insert_sql(cls, tname, col_names, obj):
        cols = []
        vals = []
        for k in col_names:
            v = obj.get(k, None)
            if v is None:
                continue
            cols.append("`{0}`".format(k))
            vals.append(":{0}".format(k))
        if not cols:
            return None
        fmt = """insert into {0} ({1}) values ({2})"""
        return fmt.format(tname, ",".join(cols), ",".join(vals))

    @classmethod
    def update_sql(cls, tname, col_names, conditions, obj):
        cols = []
        for k in col_names:
            v = obj.get(k, None)
            if v is None:
                continue
            item = "`{0}`=:{0}".format(k)
            cols.append(item)

        wheres = ["1=1"]
        for k in conditions:
            v = obj.get(k, None)
            if v is None:
                continue
            item = "`{0}`=:{0}".format(k)
            wheres.append(item)
            
        if not cols:
            return None
        fmt = """update {0} set {1} where {2}"""
        return fmt.format(tname, ",".join(cols), " and ".join(wheres))
