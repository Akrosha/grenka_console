# test command

def updatedata(self, args = []):
    """debug update_data database\n\t{name} <str:table> $ <str:data> $ <str:condition>"""
    self.database.update_data(args[0], args[1], args[2])