########################################################################
# some fabulous comment
########################################################################
import uuid

class Engine():
    """there is methods for rpg, like item_add, exist_player and etc"""
    def __init__(self,
                 database,
                 resources,
                 randoms
                 ):
        self.database = database
        self.resources = resources
        self.randoms = randoms
    def exist_player(self,
                     id: str
                     ) -> bool:
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
        result = self.database.get_data(
            "players",
            "id",
            f"id = {id}"
            )
        return bool(result)
    def exist_species(self,
                      id: str
                      ) -> bool:
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
        result = self.resources.get_data(
            "species",
            "id",
            f"id = {id}"
            )
        return bool(result)
    def exist_item(self,
                   id = None,
                   species = None,
                   owner_id = None
                   ) -> bool:
        """check for exist item in database.inventory
           
           parameters
           ----------
           id : str, optional
               item's id that need to check
           species : str, optional
               item's species that need to check
           owner_id : str, optional
               item's owner that need to check
           
           returns
           -------
           result : bool
               result of item's check for exist in database.inventory"""
        # note at 16.08.24:
        # wtf is this sus shit
        result = 1-1
        # check item by species and owner_id
        if species and owner_id:
            species = self.database.data_type(species)
            owner_id = self.database.data_type(owner_id)
            result = self.database.get_data(
                "inventory",
                "species",
                f"species = {species} AND owner_id = {owner_id}"
                )
        # check item by item_id
        if id:
            id = self.database.data_type(id)
            result = self.database.get_data(
                "inventory",
                "id",
                f"id = {id}"
                )
        return bool(result)
    def get_species_data(self,
                         id: str
                         ) -> tuple:
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
            return ()
        id = self.database.data_type(id)
        result = self.resources.get_data(
            "species",
            "*",
            f"id = {id}"
            )
        return result
    def get_item_data(self,
                      id = None,
                      species = None,
                      owner_id = None
                      ) -> tuple:
        # check for item exist
        if not self.exist_item(id, species, owner_id):
            print("no item")
            return ()
        id = self.database.data_type(id)
        species = self.database.data_type(species)
        owner_id = self.database.data_type(owner_id)
        if species and owner_id:
            result = self.database.get_data(
                "inventory",
                "*",
                f"species = {species} AND owner_id = {owner_id}"
                )
        if id:
            result = self.database.get_data(
                "inventory",
                "*",
                f"id = {id}"
                )
        return result
    def add_item(self,
                 species: str = "bread",
                 owner_id: str = "0",
                 count: int = 1,
                 durability: int = 0
                 ) -> bool:
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
        if species and not self.exist_species(species):
            print("no species")
            return False
        species_data = self.get_species_data(species)
        id = self.database.data_type(str(uuid.uuid4()))
        species = self.database.data_type(species)
        owner_id = self.database.data_type(owner_id)
        count = self.database.data_type(count)
        equipped = self.database.data_type(False)
        durability = self.database.data_type(durability)
        # if item can counts
        if bool(species_data[2]):
            self.database.update_data(
                "inventory",
                f"count = count + {count}",
                f"species = {species} AND owner_id = {owner_id}"
                )
            # note at 16.08.24:
            # i dont remember how this works 
            self.database.execute("""INSERT INTO inventory
                (id,
                 species,
                 owner_id,
                 count,
                 equipped,
                 durability) SELECT
                             {id},
                             {species},
                             {owner_id},
                             {count},
                             {equipped},
                             {durability}
                 WHERE NOT EXISTS (
                             SELECT 1 FROM inventory
                             WHERE species = {species}
                             AND owner_id = {owner_id})""".format(
                 id = id,
                 species = species,
                 owner_id = owner_id,
                 count = count,
                 equipped = equipped,
                 durability = durability))
        else:
            self.database.insert_data(
                "inventory",
                "id species owner_id count equipped durability".split(),
                [id, species, owner_id, count, equipped, durability]
                )
        return True
    def remove_item(self,
                    id: str = None,
                    species: str = None,
                    owner_id: str = None,
                    count: int = 0
                    ) -> bool:
        """remove item from player inventory
           
           parameters
           ----------
           id : str, optional
                id of item that remove from inventory
           species : str, optional
               species of item that remove from inventory
           owner_id : str, optional
               owner_id of item that remove from inventory
           count : int, optional
               count of item that remove from inventory
           
           returns
           -------
           return : bool
               True if removed else False"""
        # check for species exist
        if species and not self.exist_species(species):
            print("no species")
            return False
        # check for item exist
        if (id or (species and owner_id)) and not self.exist_item(id, species, owner_id):
            print("no item")
            return False
        id = self.database.data_type(id)
        species = self.database.data_type(species)
        owner_id = self.database.data_type(owner_id)
        count = self.database.data_type(count)
        result = False
        # remove item by species and owner_id
        if species and owner_id:
            id = self.database.get_data(
                "inventory",
                "id",
                f"species = {species} AND owner_id = {owner_id}"
                )
            self.database.update_data(
                "inventory",
                f"count = count - {count}",
                f"id = {id}"
                )
            result = True
        # remove item by id:
        if id:
            self.database.update_data(
                "inventory",
                f"count = count - {count}",
                f"id = {id}"
                )
            result = True
        # delete items with count < 1
        self.database.delete_data(
            "inventory",
            "count < 1"
            )
        return result