########################################################################
# some fabulous comment
########################################################################

import os, re
from functions.randoms import Randoms
from functions.database import Database, Resources

class Handler_cmd():
    def __init__(self, main_path):
        self.id = input("insert id: ")
        self.main_path = main_path
        self.command_list = []
        self.database = Database(os.path.join(main_path,
                                 "database", "database.sqlite3"))
        self.database.check_exist() # init tables if not exist
        self.resources = Resources(os.path.join(main_path,
                                 "resources", "resources.sqlite3"))
        self.randoms = Randoms(1) # need for random command
        self.value = None # need for run_command return
    def run_command(self, raw):
        raw_list = re.sub("\s*$", "", re.sub("^\s*\S+\s*", "", raw))
        command = re.match("[^\s]*\S+",raw)
        if command: command = command.group(0)
        args = [x for x in re.split("\s*\$\s*", raw_list) if x != ""]
        if command in self.command_list:
            exec(f"self.value = self.{command}(self=self, args=args)")
            return self.value
        else:
            return f"{command}: command is not exist"
    def add_command(self, command):
        exec(f"from commands.{command} import {command}")
        exec(f"self.{command} = {command}")
        self.command_list.append(command)