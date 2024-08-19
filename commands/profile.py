# if len(args) > 0
#   return "args_id info"
# else
#   return "sender_id info"

from functions.levels import get_level, get_experience, get_max_health

def profile(self, args = []):
    """show user profile\n\t{name}\n\t{name} <str:id>"""
    if len(args) > 0:
        id = args[0]
    else:
        id = self.id
    if not self.rpg_engine.exist_player(id):
        return f"{id} are not registered\n\ttype register <str:name>"
    player = self.database.get_data(
        "players",
        "name, location, health, experience",
        f"id = {self.database.data_type(id)}"
        )
    # [0] is important because execute returns ('name', 'location', health, experience)
    name = player[0]
    location = player[1]
    money = self.database.get_data(
        "inventory",
        "COALESCE(SUM(count), 0) AS count",
        f"species = {self.database.data_type('money')} AND owner_id = {self.database.data_type(id)}"
        )[0]
    minHP = player[2]
    XP = player[3]
    level = get_level(XP)
    maxHP = get_max_health(level)
    dexperience = [get_experience(level), get_experience(level + 1)]
    level = level + 1
    minXP = XP - dexperience[0]
    maxXP = dexperience[1] - dexperience[0]
    return f"Statistics\n\nName:\n\t{name}\nID:\n\t{id}\nLocation:\n\t{location}\nHP:\n\t{minHP}/{maxHP}:heart:\nLevel:\n\t{level}:arrow_up:\nExp:\n\t{minXP}/{maxXP} ({XP}):sparkles:\nMushrooms:\n\t{money}:mushroom:"