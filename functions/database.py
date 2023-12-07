########################################################################
# some fabulous comment
########################################################################

import json
import sqlite3

class Database():
    def __init__(self, file_path):
        self.file_path = file_path
        self.connect = sqlite3.connect(self.file_path)
        self.cursor = self.connect.cursor()
    def execute(query, fetchall = False):
        try:
            if fetchall:
                result = self.cursor.execute(query).fetchall()
            else:
                result = self.cursor.execute(query).fetchone()
            self.connect.commit()
        except:
            result = None
        return result
    def check_exist(self): # init tables if not exist
        ...