# test command

def execdat(self, args = []):
    """debug execdat\n\t{name} <str:query> $ <bool:fetchall>"""
    b = "NONE"
    if len(args) == 1:
        b = self.database.execute(args[0])
    if len(args) > 1:
        b = self.database.execute(args[0], args[1])
    return b