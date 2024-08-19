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
    """help for debugs\n\t{name}\n\t{name} <int:page>\n\t{name} <str:command>"""
    debug_list = []
    for command in self.debug_list:
        exec(f"self.value = self.{command}.__doc__.format(name=self.{command}.__name__)")
        if self.value:
            self.value = self.value.split("\n")[0]
        else:
            self.value = "None"
        debug_list.append(f"{command} - {self.value}")
    debug_list.sort()
    
    if len(args) > 0:
        command = args[0]
        if command.isdigit():
            return list_like(debug_list, "debug list", int(command), 7)
    else:
        return list_like(debug_list, "debug list", 1, 7)
    
    if command in self.command_list + self.debug_list:
        exec(f"self.value = self.{command}.__doc__.format(name=self.{command}.__name__)")
        return self.value
    else:
        return f"{command}: command is not exist"
