# test command

def rdelc(self, args = []):
    """debug delete_column resources\n\t{name} <str:table> $ <str:name>"""
    self.resources.delete_column(args[0], args[1])