def renc(self, args = []):
    """debug rename_column\n\taddc <str:table> $ <str:name> $ <str:new_name>"""
    self.database.rename_column(args[0], args[1], args[2])