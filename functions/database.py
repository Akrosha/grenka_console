########################################################################
# some fabulous comment
########################################################################

import json
import sqlite3
from typing import Optional, Any, Union, NoReturn

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
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.connect = sqlite3.connect(self.file_path)
        self.cursor = self.connect.cursor()
    def reload(self) -> NoReturn:
        """reload connect to database file"""
        self.connect.commit()
        self.connect.close()
        self.connect = sqlite3.connect(self.file_path)
        self.cursor = self.connect.cursor()
    def data_type(self, data: Any) -> Any:
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
    def add_column(table: str, name: str, type: str):
        """add column in the table
           
           parameters
           ----------
           table : str
               name of table that add column
           name : str
               name of column
           type : str
               type of data in this column"""
        if "str" == type:
            type = "TEXT"
        elif "int" == type:
            type = "INTEGER"
        else:
            type = "TEXT"
        name = name.lower()
        self.execute(f"ALTER TABLE {table} ADD COLUMN {name} {type}")
    def rename_column(table: str, name: str, new_name: str):
        """rename column in the table
           
           parameters
           ----------
           table : str
               name of table that rename column
           name : str
               name of column
           new_name : str
               new name of column"""
        name = name.lower()
        new_name = new_name.lower()
        self.execute(f"ALTER TABLE {table} RENAME COLUMN {name} TO {new_name}")
    def delete_column(table: str, name: str):
        """delete column in the table
           
           parameters
           ----------
           table : str
               name of table that delete column
           name : str
               name of column"""
        name = name.lower()
        self.execute(f"ALTER TABLE {table} DROP COLUMN {name}")
    def insert_data(table: str, keys: list, values: list):
        """insert data in the table
           
           parameters
           ----------
           table : str
               name of table that insert data
           keys : list
               list of keys
           values : list
               list of values"""
        keys = f"({', '.join(keys)})"
        values = f"({', '.join(values)})"
        self.execute(f"INSERT INTO {table} {keys} VALUES {values}")
    # TODO: FINISH THIS
    def update_data(table: str, data: str, condition: str):
        """update data in the table
           
           parameters
           ----------
           table : str
               name of table that update data
           data : str
               data that update
           condition : str
               the condition of data update"""
        self.execute(f"UPDATE {table} SET {data} WHERE {condition}")
    def delete_data(table: str, condition: str):
        """delete data in the table
        
        parameters
           ----------
           table : str
               name of table that delete data
           condition : str
               the condition of data delete"""
        self.execute(f"DELETE FROM {table} WHERE {condition}")
    def get_data(table: str, query: str, condition: str):
        """get data from the table
           
           parameters
           ----------
           table : str
               name of table that get data
           query : str
               what data need to get
           condition : str
               the condition of data get
           
           returns
           -------
           data : Any
               getting data"""
        data = self.execute(f"SELECT {query} FROM {table} WHERE {condition}")
        return data
    def execute(self, query: str, fetchall: bool = False) -> Any:
        """execute sql query
           
           parameters
           ----------
           query : str
               data to format for execute query
           fetchall : bool
               sets fetch setting
           
           returns
           -------
           return : Any
               result of execute"""
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
