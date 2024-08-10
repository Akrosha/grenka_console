# debug
#
# if len(args) > 0
#   if args[0].isDigit
#      return "debug list (page args[0])"
#   else
#      return "debug info"
# else
#   return "debug list (page 1)"

from functions.list_like import list_like

def debug(self, args = []):
    """help for debugs\n\tdebug\n\tdebug <int:page>\n\tdebug <str:command>"""
    if len(args) > 0:
        command = args[0]
        if command.isdigit():
            return list_like(self.debug_list, "debug list", int(command))
    else:
        return list_like(self.debug_list, "debug list")
    
    if command in self.command_list + self.debug_list:
        exec(f"self.value = self.{command}.__doc__")
        return self.value
    else:
        return f"{command}: command is not exist"
