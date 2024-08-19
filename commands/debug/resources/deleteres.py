# test command

def deleteres(self, args = []):
    """debug delete_data resources\n\t{name} <str:table> $ <str:condition>"""
    self.resources.delete_data(args[0], args[1])