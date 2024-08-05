# test command

def execdat(self, args = []):
    """debug execdat\n\execdat <str:query>"""
    b = self.database.execute(args[0])
    return b