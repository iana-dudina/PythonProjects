import requests

response = requests.post ('https://pokemonbattle.me:9104/pokemons', headers = {'Content-Type': 'application/json', "trainer_token": 'd16645b3b943bfd1bc45bfaa875c4000'}, json = {"name": "PokeName","photo": "https://dolnikov.ru/pokemons/albums/035.png"})

print(response.text)

response = requests.put ('https://pokemonbattle.me:9104/pokemons', headers = {'Content-Type': 'application/json', "trainer_token": 'd16645b3b943bfd1bc45bfaa875c4000'}, json = {
    "pokemon_id": 6300,
    "name": "PokeName",
    "photo": "https://dolnikov.ru/pokemons/albums/363.png"
})

print(response.text)

response = requests.post ('https://pokemonbattle.me:9104/trainers/add_pokeball', headers = {'Content-Type': 'application/json', "trainer_token": 'd16645b3b943bfd1bc45bfaa875c4000'}, json = {"pokemon_id": "6300"})

print(response.text)