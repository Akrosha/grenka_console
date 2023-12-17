########################################################################
# some fabulous comment
########################################################################

import math

# какой будет уровень при таком опыте
def get_level(experience: int) -> int:
    level = (math.sqrt(10.5*experience + 2304) - 48) / 5.25
    # (-7.5 + math.sqrt(56.25 + 10.5*experience)) / 5.25
    return int(level)

# сколько надо опыта для этого уровня
def get_experience(level: int) -> int:
    experience = 2.625*level*level + 48*level
    # 1.5*level * (1.75*level + 5)
    return math.ceil(experience)

# сколько будет лимит здоровья при таком уровне
def get_max_health(level: int) -> int:
    max_health = 20 + 4.2*level
    return int(max_health)