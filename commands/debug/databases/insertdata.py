# test command

def insertdata(self, args = []):
    """debug insert_data database\n\t{name} <str:table> $ <list:keys> $ <list:values>"""
    self.database.insert_data(args[0], args[1], args[2])