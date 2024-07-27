#

from functions.list_like import list_like

def location(self, args = []):
    """move to other location\n\tlocation\n\tlocation <int:location>"""
    id = self.id
    player = self.database.execute(
        """SELECT location FROM players
        WHERE id = {id}""".format(id = self.database.data_type(id)) )
    if player:
        # [0] is important because execute returns ('location')
        location = player[0]
        locations = eval(self.resources.execute("""SELECT paths FROM locations WHERE id = {id}""".format(id = self.resources.data_type(location)))[0])
        if len(args) == 0:
            return list_like(locations, "locations", 1, 16)
        if (len(args) > 0):
            if args[0].isdigit and int(args[0]) > 0 and len(locations) >= int(args[0]):
                self.database.execute("""UPDATE players SET location = {location} WHERE id = {id}""".format(location = self.database.data_type(locations[int(args[0])-1]), id = self.database.data_type(id)))
                return f"{id} going to {locations[int(args[0])-1]}"
            else:
                return f"syntax error: location <int:location>"
    else:
        return f"{id} are not registered\n\ttype register <str:name>"