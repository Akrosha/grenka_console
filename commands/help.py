# if len(args) > 0
#   if args[0].isDigit
#      return "command list (page args[0])"
#   else
#      return "command info"
# else
#   return "command list (page 1)"

from functions.list_like import list_like

def help(self, args = []):
    """help for commands\n\t{name}\n\t{name} <int:page>\n\t{name} <str:command>"""
    command_list = []
    for command in self.command_list:
        exec(f"self.value = self.{command}.__doc__.format(name=self.{command}.__name__)")
        if self.value:
            self.value = self.value.split("\n")[0]
        else:
            self.value = "None"
        command_list.append(f"{command} - {self.value}")
    command_list.sort()
    
    if len(args) > 0:
        command = args[0]
        if command.isdigit():
            return list_like(command_list, "command list", int(command), 7)
    else:
        return list_like(command_list, "command list", 1, 7)
    
    if command in self.command_list + self.debug_list:
        exec(f"self.value = self.{command}.__doc__.format(name=self.{command}.__name__)")
        return self.value
    else:
        return f"{command}: command is not exist"
