from functions.levels import get_level, get_experience, get_max_health

def profile(self, args = []):
    """show user profile\n\tprofile <str:id>"""
    if len(args) > 0:
        id = args[0]
    else:
        id = self.id
    player = self.database.execute(
        """SELECT name, location, money, health, experience FROM players
        WHERE id = {id}""".format(id = self.database.data_type(id)))
    if player:
        # [0] is important because execute returns ('name', 'location', money, health, experience)
        name = player[0]
        location = player[1]
        money = player[2]
        minHP = player[3]
        XP = player[4]
        level = get_level(XP)
        maxHP = get_max_health(level)
        dexperience = [get_experience(level), get_experience(level + 1)]
        level = level + 1
        minXP = XP - dexperience[0]
        maxXP = dexperience[1] - dexperience[0]
        return f"Statistics\n\nName:\n{name}\nID:\n{id}\nLocation:\n{location}\n\nHP:\n{minHP}/{maxHP}:heart:\nLevel:\n{level}:arrow_up:\nExp:\n{minXP}/{maxXP} ({XP}):sparkles:\nMushrooms:\n{money}:mushroom:"
    else:
        return f"{id} are not registered\n\ttype register <str:name>"