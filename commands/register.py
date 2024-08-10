#

def register(self, args = []):
    """register in the rpg system\n\tregister <str:name>"""
    id = self.id
    if self.rpg_engine.exist_player(id):
        name = self.database.get_data(
            "players",
            "name",
            f"id = {self.database.data_type(id)}"
            )
        # [0] is important because execute returns ('name', )
        return f"{id} is already registered with the name {name[0]}"
    
    if len(args) > 0:
        name = args[0]
    else:
        name = "Jodin"
    name = name.upper()
    
    if (len(name) > 16) or (len(name) < 2):
        return "the name must be in 3-15 characters"
    
    test_id = self.database.get_data(
        "players",
        "id",
        f"name = {self.database.data_type(name)}"
        )
    if test_id:
        # [0] is important because execute returns ('test_id', )
        return f"the name {name} has already been registered by {test_id[0]}"
        
    
    self.database.insert_data(
        "players",
        ["id", "name", "experience", "health", "bonus", "location"],
        [self.database.data_type(i) for i in [id, name, 0, 20, 0, "start_glade"]]
        )
    self.rpg_engine.add_item(species = "money", owner_id = id, count = self.randoms.getRandom(min = 256, max = 1024))
    
    return f"{id} successfully registered with the name {name}"
