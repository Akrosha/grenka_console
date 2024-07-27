# if len(args) > 0
#   return "command info"
# else
#   return "command list"

from functions.list_like import list_like

def help(self, args = []):
    """help for commands\n\thelp\n\thelp <int:page>\n\thelp <str:command>"""
    if len(args) > 0:
        command = args[0]
        if command.isdigit():
            return list_like(self.command_list, "command list", int(command))
    else:
        return list_like(self.command_list, "command list")
    
    if command in self.command_list:
        exec(f"self.value = self.{command}.__doc__")
        return self.value
    else:
        return f"{command}: command is not exist"
