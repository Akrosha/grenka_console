def execres(self, args = []):
    """debug execres\n\execres <str:query>"""
    b = self.resources.execute(args[0])
    return b