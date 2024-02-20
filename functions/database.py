########################################################################
# some fabulous comment
########################################################################

import json
import sqlite3
from typing import Optional, Any, Union

class SQLite3Tool():
    """base for database and resources
       
       parameters
       ----------
       file_path : str
           path of database file
       
       attributes
       ----------
       file_path : str
           path of database file
       connect : sqlite3.connect
       cursor : sqlite3.connect.cursor"""
    def __init__(self, file_path):
        self.file_path = file_path
        self.connect = sqlite3.connect(self.file_path)
        self.cursor = self.connect.cursor()
    def reload(self) -> NoReturn:
        """reload connect to database file"""
        self.connect.commit()
        self.connect.close()
        self.connect = sqlite3.connect(self.file_path)
        self.cursor = self.connect.cursor()
    def data_type(self, data: Any) ->:
        """format data for execute query
           
           parameters
           ----------
           data : Any
               data to format for execute query
           
           returns
           -------
           return : Any
               formatted data for execute query"""
        if isinstance(data, bool):
            return f"{int(data)}"
        elif isinstance(data, (int, float)):
            return f"{data}"
        elif isinstance(data, str):
            return f"'{data}'"
        elif isinstance(data, (dict, list)):
            return f"{json.dumps(data)}"
    def execute(self, query, fetchall : bool = False):
        try:
            if fetchall:
                result = self.cursor.execute(query).fetchall()
            else:
                result = self.cursor.execute(query).fetchone()
            self.connect.commit()
        except Exception as e:
            print(e)
            result = None
        return result

class Database(SQLite3Tool):
    def check_exist(self): # init tables if not exist
        self.execute("""CREATE TABLE IF NOT EXISTS players
                        (id TEXT,
                        name TEXT,
                        experience INTEGER,
                        health INTEGER,
                        bonus INTEGER,
                        location TEXT,
                        in_fight INTEGER)""")
        self.execute("""CREATE TABLE IF NOT EXISTS inventory
                        (item_id TEXT,
                        species TEXT,
                        owner_id TEXT,
                        count INTEGER,
                        equipped INTEGER,
                        durability INTEGER)""")

class Resources(SQLite3Tool):
    def check_exist(self):
        self.execute("""CREATE TABLE IF NOT EXISTS species
                        (id TEXT,
                        type TEXT,
                        is_counts INTEGER,
                        is_equips INTEGER,
                        cost INTEGER,
                        durability INTEGER,
                        slots_count INTEGER,
                        health INTEGER,
                        damage INTEGER,
                        defence INTEGER)""")
        self.execute("""CREATE TABLE IF NOT EXISTS locations
                        (id TEXT,
                        mobs BLOB,
                        paths BLOB)""")
        self.execute("""CREATE TABLE IF NOT EXISTS shop
                        (id TEXT,
                        item_id TEXT,
                        item_count INTEGER,
                        price_id TEXT,
                        price_count INTEGER)""")
        self.execute("""CREATE TABLE IF NOT EXISTS trade
                        (id TEXT,
                        owner_id TEXT,
                        item_id TEXT,
                        price_id TEXT)""")