# if (bonusFROMplayers - time()) < 0
#   rpg_engine.add_item("money", id, random(256, 1024))
#   bonusFROMplayers = time() + 86400
#   return "text"
# else
#   return "text"



from time import time

def bonus(self, args = []):
    """get a daily bonus\n\tbonus"""
    id = self.id
    if self.rpg_engine.exist_player(id):
        bonus = self.database.get_data(
            "players",
            "bonus",
            f"id = {self.database.data_type(id)}"
            )
        # [0] is important because execute returns ('bonus', )
        test_bonus = bonus[0] - int(time())
        if test_bonus < 0:
            new_bonus = int(time()) + 86400
            money = self.randoms.getRandom(min = 256, max = 1024)
            self.database.update_data(
                "players",
                f"bonus = {self.database.data_type(new_bonus)}",
                f"id = {self.database.data_type(id)}"
                )
            self.rpg_engine.add_item(species = "money", owner_id = id, count = money)
            return f"{id} get {money}:mushroom: from the daily bonus, the next one will be {new_bonus}"
        else:
            return f"{id} have already received :mushroom: today, the next one will be {bonus[0]}"
    else:
        return f"{id} are not registered\n\ttype register <str:name>"
