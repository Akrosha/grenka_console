# test command

def raddc(self, args = []):
    """debug add_column resources\n\t{name} <str:table> $ <str:name> $ <str:type>"""
    self.resources.add_column(args[0], args[1], args[2])