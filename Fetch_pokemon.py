import requests

def fetch_pokemon_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    response = requests.get(url)
    data = response.json()
    name = data['name']
    abilities = [ability['ability']['name'] for ability in data['abilities']]
    weight = data['weight']
    return name, abilities, weight

def calculate_average_weight(pokemon_list):
    total_weight = 0
    for pokemon in pokemon_list:
        _, _, weight = fetch_pokemon_data(pokemon)
        total_weight += weight
    return total_weight / len(pokemon_list)

pokemon_names = ["pikachu", "bulbasaur", "charmander"]
for name in pokemon_names:
    name, abilities, weight = fetch_pokemon_data(name)
    print(f"Name: {name}")
    print(f"Abilities: {abilities}")
    print(f"Weight: {weight}")

avg_weight = calculate_average_weight(pokemon_names)
print(f"Average Weight: {avg_weight}")

