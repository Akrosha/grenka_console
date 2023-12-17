def profile(self, args = []):
    """show user profile\n\tprofile <str:id>"""
    if len(args) > 0:
        id = args[0]
    else:
        id = self.id
    player = self.database.execute(
        """SELECT name, money FROM players
        WHERE id = {id}""".format(id = self.database.data_type(id)))
    if player:
        # [0] is important because execute returns ('name', money)
        return f"{id}'s profile\nname: {player[0]}\nbalance: {player[1]}:mushroom:"
    else:
        return f"{id} are not registered\n\ttype register <str:name>"