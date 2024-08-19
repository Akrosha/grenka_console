# test command

def insertres(self, args = []):
    """debug insert_data resources\n\t{name} <str:table> $ <list:keys> $ <list:values>"""
    self.resources.insert_data(args[0], args[1], args[2])