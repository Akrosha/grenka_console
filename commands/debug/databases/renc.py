# test command

def renc(self, args = []):
    """debug rename_column database\n\t{name} <str:table> $ <str:name> $ <str:new_name>"""
    self.database.rename_column(args[0], args[1], args[2])