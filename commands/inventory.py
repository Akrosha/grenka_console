# if len(args) > 0
#   if args[0].isDigit
#      return "inventory (page args[0])"
#   else
#      return "syntax error"
# else
#   return "inventory (page 1)"

from functions.list_like import list_like

def inventory(self, args = []):
    """show inventory\n\t{name} <int:page>"""
    id = self.id
    if not self.rpg_engine.exist_player(id):
        return f"{id} are not registered\n\ttype register <str:name>"
    inventory = self.database.get_data(
        "inventory",
        "species, count",
        f"owner_id = {self.database.data_type(id)}",
        fetchall = True)
    
    for i in range(len(inventory)):
        if inventory[i][1] > 1:
            inventory[i] = f"{inventory[i][0]}: {inventory[i][1]}"
        else:
            inventory[i] = f"{inventory[i][0]}"
    
    if (len(args) > 0):
        if args[0].isdigit:
            return list_like(inventory, "inventory", int(args[0]), 7)
        else:
            return f"syntax error: inventory <int:page>"
    else:
        return list_like(inventory, "inventory", 1, 7)