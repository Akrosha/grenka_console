# test command

def getdata(self, args = []):
    """debug get_data database\n\t{name} <str:table> $ <str:query> $ <str:condition> $ <bool:fetchall>"""
    if args[3]:
        self.database.get_data(args[0], args[1], args[2], args[3])
    else:
        self.database.get_data(args[0], args[1], args[2])