# test command

def execdat(self, args = []):
    """debug execdat\n\execdat <str:query> $ <bool:fetchall>"""
    b = "NONE"
    if len(args) == 1:
        b = self.database.execute(args[0])
    if len(args) > 1:
        b = self.database.execute(args[0], args[1])
    return b