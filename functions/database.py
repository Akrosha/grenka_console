########################################################################
# some fabulous comment
########################################################################

import json
import sqlite3

class SQLite3Tool():
    def __init__(self, file_path):
        self.file_path = file_path
        self.connect = sqlite3.connect(self.file_path)
        self.cursor = self.connect.cursor()
    def reload(self):
        self.connect.commit()
        self.connect.close()
        self.connect = sqlite3.connect(self.file_path)
        self.cursor = self.connect.cursor()
    def data_type(self, data):
        if isinstance(data, bool):
            return f"{int(data)}"
        elif isinstance(data, (int, float)):
            return f"{data}"
        elif isinstance(data, str):
            return f"'{data}'"
        elif isinstance(data, (dict, list)):
            return f"{json.dumps(data)}"
    def execute(self, query, fetchall = False):
        try:
            if fetchall:
                result = self.cursor.execute(query).fetchall()
            else:
                result = self.cursor.execute(query).fetchone()
            self.connect.commit()
        except:
            result = None
        return result

class Database(SQLite3Tool):
    def check_exist(self): # init tables if not exist
        self.execute("""CREATE TABLE IF NOT EXISTS players
                        (id TEXT,
                        name TEXT,
                        money INTEGER,
                        experience INTEGER,
                        health INTEGER,
                        bonus INTEGER,
                        location TEXT)""")
        self.execute("""CREATE TABLE IF NOT EXISTS inventory
                        (item_id TEXT,
                        species TEXT,
                        owner_id TEXT,
                        count INTEGER,
                        equipped INTEGER,
                        durability INTEGER)""")

class Resources(SQLite3Tool):
    def check_exist(self):
        ...