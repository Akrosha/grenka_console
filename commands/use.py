# 

def use(self, args = []):
    """use item from inventory\n\t{name}"""
    id = self.id
    if not self.rpg_engine.exist_player(id):
        return f"{id} are not registered\n\ttype register <str:name>"
    return f"use!"