# get pokemon data from api
import requests
from pokemon_types import pokemon_type_matrix
def fetch_pokemon_data(pokemon_name):
    url = "https://pokeapi.co/api/v2/pokemon/"+str(pokemon_name).lower()
    response = requests.get(url)
    if response.status_code == 200:
        print("[System] >>> Data received successfully! <<<\n")
        pokemon_data = response.json()
        name = pokemon_data['name'].capitalize()
        types_list = []
        for type_info in pokemon_data['types']:
            types_list.append(type_info['type']['name'].title())
        hp = pokemon_data['stats'][0]['base_stat']
        attack = pokemon_data['stats'][1]['base_stat']
        defense = pokemon_data['stats'][2]['base_stat']
        speed = pokemon_data['stats'][5]['base_stat']
        abilities_list = []
        for ability_info in pokemon_data['abilities']:
            ability_name = ability_info['ability']['name'].replace('-', ' ').title()
            if ability_info['is_hidden']:
                abilities_list.append(f"{ability_name} (Hidden)")
            else:
                abilities_list.append(ability_name)
        moves_list = []
        for move_info in pokemon_data['moves'][:5]:
            move_name = move_info['move']['name'].replace('-', ' ').title()
            moves_list.append(move_name)
        print(f"\n====================== STAT BANK: {name} ======================")
        print(f"Typing     : {' / '.join(types_list)}")
        pokemon_type_matrix(types_list)
        print(f"Core Stats : HP: {hp} | Atk: {attack} | Def: {defense} | Speed: {speed}")
        print(f"Abilities  : {', '.join(abilities_list)}")
        print(f"Movepool   : {', '.join(moves_list)}")
        print("================================================================")
    elif response.status_code == 404:
        print(f"\n[Error] The API could not find a Pokémon named '{pokemon_name}'. Check your spelling!")
    else:
        print(f"\n[Error] The internet connection failed. Code: {response.status_code}")
if __name__ == "__main__":
    print("Welcome to the Global Pokedex Terminal")
    while True:
        target = input("\nEnter a pokemon name to scan (or type 'exit' to quit): ").strip()
        if target.lower() == 'exit':
            break
        fetch_pokemon_data(target)