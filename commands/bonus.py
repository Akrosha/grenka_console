from time import time

def bonus(self, args = []):
    """get a daily bonus\n\tbonus"""
    id = self.id
    bonus = self.database.execute(
        """SELECT bonus FROM players
        WHERE id = {id}""".format(id = self.database.data_type(id)) )
    if bonus:
        # [0] is important because execute returns ('bonus', )
        test_bonus = bonus[0] - int(time())
        if test_bonus < 0:
            new_bonus = int(time()) + 86400
            money = self.randoms.getRandom(min = 256, max = 1024)
            self.database.execute(
                """UPDATE players
                SET bonus = {bonus}
                WHERE id = {id}""".format(
                    id = self.database.data_type(id),
                    bonus = self.database.data_type(new_bonus)) )
            self.rpg_engine.add_item(species = "money", owner_id = id, count = money)
            return f"{id} get {money}:mushroom: from the daily bonus, the next one will be {new_bonus}"
        else:
            return f"{id} have already received :mushroom: today, the next one will be {bonus[0]}"
    else:
        return f"{id} are not registered\n\ttype register <str:name>"