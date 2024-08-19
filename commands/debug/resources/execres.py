# test command

def execres(self, args = []):
    """debug execres\n\t{name} <str:query> $ <bool:fetchall>"""
    b = "NONE"
    if len(args) == 1:
        b = self.resources.execute(args[0])
    if len(args) > 1:
        b = self.resources.execute(args[0], args[1])
    return b