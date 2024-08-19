# test command

def updateres(self, args = []):
    """debug update_data resources\n\t{name} <str:table> $ <str:data> $ <str:condition>"""
    self.resources.update_data(args[0], args[1], args[2])