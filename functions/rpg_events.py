########################################################################
# some fabulous comment
########################################################################
import uuid

class Engine():
    def __init__(self, database, resources, randoms):
        self.database = database
        self.resources = resources
        self.randoms = randoms
    def exist_species(self, id):
        id = self.database.data_type(id)
        result = self.resources.execute("""SELECT id FROM species
                                   WHERE id = {id}""".format(
                                       id = id))
        return bool(result)
    
    def exist_item(self, item_id = None, species = None, owner_id = None):
        if species and owner_id:
            species = self.database.data_type(species)
            owner_id = self.database.data_type(owner_id)
            result = self.database.execute("""SELECT species FROM inventory
                                   WHERE species = {species}
                                   AND owner_id = {owner_id}""".format(
                                       species = species,
                                       owner_id = owner_id))
        if item_id:
            item_id = self.database.data_type(item_id)
            result = self.database.execute("""SELECT item_id FROM inventory
                                   WHERE item_id = {item_id}""".format(
                                       item_id = item_id))
        return bool(result)
    def get_species_data(self, id):
        if not self.exist_species(id):
            print("no species")
            return "no species"
        id = self.database.data_type(id)
        result = self.resources.execute("""SELECT * FROM species
                                   WHERE id = {id}""".format(
                                       id = id))
        return result
    def add_item(self,
                 species = "bread",
                 owner_id = 0,
                 count = 1,
                 durability = 0):
        # check for species exist
        if not self.exist_species(species):
            print("no species")
            return "no species"
        species_data = self.get_species_data(species)
        item_id = self.database.data_type(str(uuid.uuid4()))
        species = self.database.data_type(species)
        owner_id = self.database.data_type(owner_id)
        count = self.database.data_type(count)
        equipped = self.database.data_type(False)
        durability = self.database.data_type(durability)
        # if item can counts 8d1580b8-c1d1-4dfe-baa6-d7dff1223995
        if bool(species_data[2]):
            self.database.execute("""UPDATE inventory
                 SET count = count + {count}
                             WHERE species = {species}
                             AND owner_id = {owner_id}""".format(
                 item_id = item_id,
                 species = species,
                 owner_id = owner_id,
                 count = count,
                 equipped = equipped,
                 durability = durability))
            
            self.database.execute("""INSERT INTO inventory
                (item_id,
                 species,
                 owner_id,
                 count,
                 equipped,
                 durability) SELECT
                             {item_id},
                             {species},
                             {owner_id},
                             {count},
                             {equipped},
                             {durability}
                 WHERE NOT EXISTS (
                             SELECT 1 FROM inventory
                             WHERE species = {species}
                             AND owner_id = {owner_id})""".format(
                 item_id = item_id,
                 species = species,
                 owner_id = owner_id,
                 count = count,
                 equipped = equipped,
                 durability = durability))
        else:
            self.database.execute("""INSERT INTO inventory
                (item_id,
                 species,
                 owner_id,
                 count,
                 equipped,
                 durability) VALUES
                            ({item_id},
                             {species},
                             {owner_id},
                             {count},
                             {equipped},
                             {durability})""".format(
                 item_id = item_id,
                 species = species,
                 owner_id = owner_id,
                 count = count,
                 equipped = equipped,
                 durability = durability))