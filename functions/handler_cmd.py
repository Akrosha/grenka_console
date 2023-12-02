########################################################################
# some fabulous comment
########################################################################

from functions.randoms import Randoms

class Handler_cmd():
    def __init__(self):
        self.command_list = []
        self.randoms = Randoms(1) # need for random command
        self.value = None # need for run_command return
    def run_command(self, raw):
        raw_list = raw.split(" ")
        command = raw_list[0]
        args = raw_list[1:]
        if command in self.command_list:
            exec(f"self.value = self.{command}(self = self, args = args)")
            return self.value
        else:
            return f"{command}: command is not exist"
    def add_command(self, command):
        exec(f"from commands.{command} import {command}")
        exec(f"self.{command} = {command}")
        self.command_list.append(command)