# test command

def addc(self, args = []):
    """debug add_column database\n\t{name} <str:table> $ <str:name> $ <str:type>"""
    self.database.add_column(args[0], args[1], args[2])