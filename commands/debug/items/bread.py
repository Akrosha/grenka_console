# test command
#
# rpg_engine.add_item("bread", id, 1)

from time import time

def bread(self, args = []):
    """test get a bread\n\t{name}"""
    id = self.id
    if not self.rpg_engine.exist_player(id):
        return f"{id} are not registered\n\ttype register <str:name>"
    self.rpg_engine.add_item(species = "bread", owner_id = id, count = 1)
    return f"{id} get bread"