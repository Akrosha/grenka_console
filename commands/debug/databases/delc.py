# test command

def delc(self, args = []):
    """debug delete_column database\n\t{name} <str:table> $ <str:name>"""
    self.database.delete_column(args[0], args[1])