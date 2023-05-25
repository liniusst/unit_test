# pylint: disable= missing-docstring
import random
from typing import Dict, Optional
import requests
from pokemon import Statistic, Pokemon

POKEMON_ENDPOINT = "https://pokeapi.co/api/v2/pokemon/"
STATS_ENDPOINT = "https://pokeapi.co/api/v2/stat/"


def get_random_pokemon() -> Dict[str, str]:
    pokemon_id = random.randint(1, 1010)
    pokemon = requests.get(f"{POKEMON_ENDPOINT}{1}", timeout=2)
    return pokemon.json()


def get_pokemon_stat():
    pokemon_stats_response = requests.get({STATS_ENDPOINT}, timeout=2)
    return pokemon_stats_response.json()


def convert_json_to_pokemon(api_response: Dict[str, str]) -> Pokemon:
    name = api_response["name"]
    response_stats = api_response["stats"]
    stats = []
    for response_stat in response_stats:
        stats.append(
            Statistic(response_stat["base_stat"], response_stat["stat"]["name"])
        )
    return Pokemon(name, stats)


def get_all_stats_names():
    stats_name = []
    stats = requests.get(STATS_ENDPOINT, timeout=2)
    stats_json = stats.json()
    for stat in stats_json["results"]:
        stats_name.append(stat["name"])
    return stats_name


def choose_winner(pokemon_one: Pokemon, pokemon_two: Pokemon) -> Optional[Pokemon]:
    all_stats = get_all_stats_names()
    p1_score = 0
    p2_score = 0
    for statistic in all_stats:
        p1_points = pokemon_one.get_statistic_base_stat(statistic)
        p2_points = pokemon_two.get_statistic_base_stat(statistic)
        if p1_points > p2_points:
            p1_score += 1
        elif p2_points > p1_points:
            p2_score += 1

    if p1_score > p2_score:
        return pokemon_one
    elif p2_score > p1_score:
        return pokemon_two
    else:
        return None


# convert_json_to_pokemon(get_random_pokemon())
pirmas = convert_json_to_pokemon(get_random_pokemon())
# antras = convert_json_to_pokemon(get_random_pokemon())
print(pirmas)

# skaiciuojam = choose_winner(pirmas, antras)
# print(skaiciuojam.name)

# a = get_random_pokemon()
# print(a["stats"])
# print(a["stats"])
