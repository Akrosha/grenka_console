# 

def trade(self, args = []):
    """trades place\n\t{name} list $ <page:int>\n\t{name} buy $ <slot_id:str>\n\t{name} sell $ <item:str> $ <count:int> $ <item:str> $ <count:int>"""
    id = self.id
    if not self.rpg_engine.exist_player(id):
        return f"{id} are not registered\n\ttype register <str:name>"
    return f"trade!"