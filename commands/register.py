def register(self, args = []):
    id = self.id
    name = self.database.execute(
        """SELECT name FROM players
        WHERE id = {id}""".format(id = self.database.data_type(id)))
    if name:
        # [0] is important because execute returns ('name', )
        return f"{id} is already registered with the name {name[0]}"
    
    if len(args) > 0:
        name = args[0]
    else:
        name = "Jodin"
    name = name.upper()
    
    if (len(name) > 16) or (len(name) < 2):
        return "the name must be in 3-15 characters"
    
    test_id = self.database.execute(
        """SELECT id FROM players
           WHERE name = {name}""".format(
                name = self.database.data_type(name)) )
    if test_id:
        # [0] is important because execute returns ('test_id', )
        return f"the name {name} has already been registered by {test_id[0]}"
        
    
    self.database.execute(
        """INSERT INTO
           players (id,
                    name,
                    money,
                    experience,
                    health,
                    bonus,
                    location)
           VALUES ({id},
                   {name},
                   {money},
                   {experience},
                   {health},
                   {bonus},
                   {location})""".format(
                       id = self.database.data_type(id),
                       name = self.database.data_type(name),
                       money = self.database.data_type(
                           self.randoms.getRandom(
                               min = 256, max = 1024)),
                       experience = self.database.data_type(0),
                       health = self.database.data_type(20),
                       bonus = self.database.data_type(0),
                       location = self.database.data_type(
                           "start_glade")) )
    
    return f"{id} successfully registered with the name {name}"