# test command

def rrenc(self, args = []):
    """debug rename_column resources\n\t{name} <str:table> $ <str:name> $ <str:new_name>"""
    self.resources.rename_column(args[0], args[1], args[2])