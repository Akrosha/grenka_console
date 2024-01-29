########################################################################
# some fabulous comment
########################################################################

class Engine():
    def __init__(self, database, resources, randoms):
        self.database = database
        self.resources = resources
        self.randoms = randoms
    def exist_species(self, id):
        id = self.date_type(id)
        result = resources.execute("""SELECT id FROM species
                                   WHERE id = {id}""".format(
                                       id = id))
        return bool(result)
    def exist_item(self, item_id = None, species = None):
        if species:
            species = self.date_type(species)
            result = database.execute("""SELECT species FROM inventory
                                   WHERE species = {species}""".format(
                                       species = species))
        if item_id:
            item_id = self.date_type(item_id)
            result = database.execute("""SELECT item_id FROM inventory
                                   WHERE item_id = {item_id}""".format(
                                       item_id = item_id))
        return bool(result)
    def add_item(self,
                 species = "bread",
                 owner_id = 0,
                 count = 1,
                 durability = 0):
        if not self.exist_species(species):
            print("no species")
            return "no species"
        if self.exist_item(species = species):
            ...