# test command

def getres(self, args = []):
    """debug get_data resources\n\t{name} <str:table> $ <str:query> $ <str:condition> $ <bool:fetchall>"""
    if args[3]:
        self.resources.get_data(args[0], args[1], args[2], args[3])
    else:
        self.resources.get_data(args[0], args[1], args[2])