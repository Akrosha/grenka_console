# 

def drop(self, args = []):
    """drop item from inventory\n\t{name} <int:item> $ <int:count>"""
    id = self.id
    if not self.rpg_engine.exist_player(id):
        return f"{id} are not registered\n\ttype register <str:name>"
    inventory = self.database.get_data(
        "inventory",
        "id, species, count",
        f"owner_id = {self.database.data_type(id)}",
        fetchall = True)
    
    if len(inventory) == 0:
        return f"inventory is empty"
    
    if (len(args) == 1) and args[0].isdigit():
        if (int(args[0]) - 1) in range(len(inventory)):
            self.rpg_engine.remove_item(
                id = inventory[int(args[0]) - 1][0],
                count = 1
                )
            return f"drop {inventory[int(args[0]) - 1][1]} in count 1"
        else:
            return
    elif (len(args) > 1) and args[0].isdigit() and args[1].isdigit():
        if (int(args[0]) - 1) in range(len(inventory)):
            if int(args[1]) > inventory[int(args[0]) - 1][2]:
                args[1] = inventory[int(args[0]) - 1][2]
            self.rpg_engine.remove_item(
                id = inventory[int(args[0]) - 1][0],
                count = int(args[1])
                )
            return f"drop {inventory[int(args[0]) - 1][1]} in count {args[1]}"
        else:
            return
    else:
        return f"syntax error: drop <int:item> $ <int:count>"