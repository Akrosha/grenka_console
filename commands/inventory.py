#

def inventory(self, args = []):
    """interact with inventory\n\tinventory"""
    id = self.id
    if self.rpg_engine.exist_player(id):
        return f"some text"
    else:
        return f"{id} are not registered\n\ttype register <str:name>"