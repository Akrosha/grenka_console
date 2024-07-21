def addc(self, args = []):
    """debug add_column\n\taddc <str:table> <str:name> <str:type>"""
    self.database.add_column(args[0], args[1], args[2])