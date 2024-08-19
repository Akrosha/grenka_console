# test command

def deletedata(self, args = []):
    """debug delete_data database\n\t{name} <str:table> $ <str:condition>"""
    self.database.delete_data(args[0], args[1])