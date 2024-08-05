########################################################################
# some fabulous comment
########################################################################
import uuid

class Engine():
    """there is methods for rpg, like item_add, exist_player and etc"""
    def __init__(self, database, resources, randoms):
        self.database = database
        self.resources = resources
        self.randoms = randoms
    def exist_player(self, id: str) -> bool:
        """check for exist player in database.players
           
           parameters
           ----------
           id : str
               user's id that need to check
           
           returns
           -------
           result : bool
               result of user's check for exist in database.players"""
        id = self.database.data_type(id)
        result = self.database.execute("""SELECT id FROM players
                                   WHERE id = {id}""".format(
                                       id = id))
        return bool(result)
    def exist_species(self, id: str) -> bool:
        """check for exist species in resources.species
           
           parameters
           ----------
           id : str
               species's id that need to check
           
           returns
           -------
           result : bool
               result of species's check for exist in resources.species"""
        id = self.database.data_type(id)
        result = self.resources.execute("""SELECT id FROM species
                                   WHERE id = {id}""".format(
                                       id = id))
        return bool(result)
    def exist_item(self, item_id = None, species = None, owner_id = None) -> bool:
        """check for exist item in database.inventory
           
           parameters
           ----------
           item_id : str, optional
               item's id that need to check
           species : str, optional
               item's species that need to check
           owner_id : str, optional
               item's owner that need to check
           
           returns
           -------
           result : bool
               result of item's check for exist in database.inventory"""
        result = 1-1
        # check item by species and owner_id
        if species and owner_id:
            species = self.database.data_type(species)
            owner_id = self.database.data_type(owner_id)
            result = self.database.execute("""SELECT species FROM inventory
                                   WHERE species = {species}
                                   AND owner_id = {owner_id}""".format(
                                       species = species,
                                       owner_id = owner_id))
        # check item by item_id
        if item_id:
            item_id = self.database.data_type(item_id)
            result = self.database.execute("""SELECT item_id FROM inventory
                                   WHERE item_id = {item_id}""".format(
                                       item_id = item_id))
        return bool(result)
    def get_species_data(self, id: str) -> tuple:
        """get species data from resources.species
           
           parameters
           ----------
           id : str
               species's id that need to get data
           
           returns
           -------
           result : tuple
               data of species like
               ('id', 'type', is_counts, is_equips, cost, durability,
                slots_count, health, damage, defence)"""
        if not self.exist_species(id):
            print("no species")
            return "no species"
        id = self.database.data_type(id)
        result = self.resources.execute("""SELECT * FROM species
                                   WHERE id = {id}""".format(
                                       id = id))
        return result
    def add_item(self,
                 species: str = "bread",
                 owner_id: str = "0",
                 count: int = 1,
                 durability: int = 0) -> bool:
        """add item in player inventory
           
           parameters
           ----------
           species : str, optional
               species of item that add to inventory
           owner_id : str, optional
               owner_id of item that add to inventory
           count : int, optional
               count of item that add to inventory
           durability : int, optional
               durability of item that add to inventory
           
           returns
           -------
           return : bool
               False if species not exist else True"""
        # check for species exist
        if not self.exist_species(species):
            print("no species")
            return False
        species_data = self.get_species_data(species)
        item_id = self.database.data_type(str(uuid.uuid4()))
        species = self.database.data_type(species)
        owner_id = self.database.data_type(owner_id)
        count = self.database.data_type(count)
        equipped = self.database.data_type(False)
        durability = self.database.data_type(durability)
        # if item can counts
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
        return True