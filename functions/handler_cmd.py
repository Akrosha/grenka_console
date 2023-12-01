########################################################################
# some fabulous comment
########################################################################

class Handler_cmd():
    def __init__(self):
        pass
    def run_command(self, raw):
        raw_list = raw.split(" ")
        command = raw_list[0]
        args = raw_list[1:]
        exec(f"self.{command}(args = args)")
    def add_command(self, command):
        exec(f"from commands.{command} import {command}")
        exec(f"self.{command} = {command}")