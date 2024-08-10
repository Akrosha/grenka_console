########################################################################
# some fabulous comment
########################################################################

import os, re
from functions.randoms import Randoms
from functions.rpg_events import Engine
from functions.database import Database, Resources

class Handler_cmd():
    """handle commands - add and run
       
       parameters
       ----------
       main_path : str
           path to main.py file
       
       attributes
       ----------
       id : str
           id of player that send a message
       main_path : str
           path to main.py file
       command_list : List
           list with command names
       database : functions.database.Database
            functions.database.Database
       resources : functions.database.Resources
            functions.database.Resources
       randoms : functions.randoms.Randoms
            functions.randoms.Randoms
       rps_engine : functions.rpg_events.Engine
            functions.rpg_events.Engine
       value : Any
           need for exec() returns in self.run_command()"""
    def __init__(self, main_path: str):
        self.id = input("insert id: ")
        self.main_path = main_path
        self.command_list = []
        self.debug_list = []
        self.database = Database(os.path.join(main_path,
                                 "database", "database.sqlite3"))
        self.database.check_exist() # init tables if not exist
        self.resources = Resources(os.path.join(main_path,
                                   "resources", "resources.sqlite3"))
        self.resources.check_exist() # init tables if not exist
        self.randoms = Randoms(1) # need for random command
        self.rpg_engine = Engine(self.database, self.resources, 
                                 self.randoms)
        self.value = None # need for exec() returns
    def run_command(self, raw):
        raw_list = re.sub("\s*$", "", re.sub("^\s*\S+\s*", "", raw))
        command = re.match("[^\s]*\S+",raw)
        if command: command = command.group(0)
        args = [x for x in re.split("\s*\$\s*", raw_list) if x != ""]
        # print(args)
        if command in self.command_list + self.debug_list:
            exec(f"self.value = self.{command}(self=self, args=args)")
            return self.value
        else:
            return f"{command}: command is not exist"
    def add_command(self, command, path):
        exec(f"from {'.'.join(path)}.{command} import {command}")
        exec(f"self.{command} = {command}")
        self.command_list.append(command)
    def add_debug(self, command, path):
        exec(f"from {'.'.join(path)}.{command} import {command}")
        exec(f"self.{command} = {command}")
        self.debug_list.append(command)