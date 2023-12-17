def help(self, args = []):
    """help for commands\n\thelp <str:command>"""
    if len(args) > 0:
        command = args[0]
    else:
        return "\n".join(self.command_list)
    
    if command in self.command_list:
        exec(f"self.value = self.{command}.__doc__")
        return self.value
    else:
        return f"{command}: command is not exist"