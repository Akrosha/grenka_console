from time import time

def bread(self, args = []):
    """test get a bread\n\tbread"""
    id = self.id
    bonus = self.database.execute(
        """SELECT bonus FROM players
        WHERE id = {id}""".format(id = self.database.data_type(id)) )
    if bonus:
        self.rpg_engine.add_item(species = "bread", owner_id = id, count = 1)
        return f"{id} get bread"
    else:
        return f"{id} are not registered\n\ttype register <str:name>"