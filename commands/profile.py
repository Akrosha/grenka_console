def profile(self, args = []):
    if len(args) > 0:
        id = args[0]
    else:
        id = self.id
    name = self.database.execute(
        """SELECT name FROM players
        WHERE id = {id}""".format(id = self.database.data_type(id)))
    if name:
        # [0] is important because execute returns ('name', )
        return f"{id}'s name is {name[0]}"
    else:
        return f"{id} are not registered\n\ttype register <str:name>"