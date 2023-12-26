
import requests

class Pokemon_Data_Model():

    def __init__(self, base_url):
        self.base_url = base_url


    def get_pokemon(self, pokemon_name_or_id):

        try:

            pokemon_by_name = requests.get(f"{self.base_url}/pokemon/{pokemon_name_or_id}")

            if pokemon_by_name.status_code != 200:
                print("Here")
                raise Exception("Could not find pokemon data!")
            
            poke_data = pokemon_by_name.json()
            print(poke_data['types'][0]['type']['name'])
            name = poke_data['name']
            type_poke = poke_data['types'][0]['type']['name']
            image = poke_data["sprites"]["front_default"]
            abilities = []
            for ability in poke_data['abilities']:
                abilities.append(ability['ability']['name'])



            p_obj = Pokemon(image, name, type_poke, abilities, poke_data['height'], poke_data['weight'])
            return p_obj
        

        



        except Exception:
            print("Oops error! Could not find pokemon by name!")
            return None
        

    
        

   

class Pokemon:
    

    def __init__(self, image, name, type_poke, abilities, height, weight):
        self.image = image
        self.name = name
        self.type_poke = type_poke
        self.abilities = abilities
        self.height = height
        self.weight = weight

    
    

        
