import unittest
from unittest import mock
from main import get_all_stats_names, get_random_pokemon, convert_json_to_pokemon
from pokemon import Pokemon, Statistic


def mocked_requests_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    if args[0] == "https://pokeapi.co/api/v2/stat/":
        return MockResponse(
            {
                "results": [
                    {"name": "hp"},
                    {"name": "attack"},
                    {"name": "defense"},
                    {"name": "special-attack"},
                    {"name": "special-defense"},
                    {"name": "speed"},
                    {"name": "accuracy"},
                    {"name": "evasion"},
                ],
            },
            200,
        )


def mocked_pokemon_requests_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    if args[0] == "https://pokeapi.co/api/v2/pokemon/":
        return MockResponse(
            Pokemon(
                name="bulbasaur",
                stats=[
                    Statistic(base_stat=45, name="hp"),
                    Statistic(base_stat=49, name="attack"),
                    Statistic(base_stat=49, name="defense"),
                    Statistic(base_stat=65, name="special-attack"),
                    Statistic(base_stat=65, name="special-defense"),
                    Statistic(base_stat=45, name="speed"),
                ],
            ),
            200,
        )


class TestIntegration(unittest.TestCase):
    @mock.patch("requests.get", side_effect=mocked_requests_get)
    def test_getting_all_stat_names(self, mock_request):
        stat_names = get_all_stats_names()
        self.assertEqual(
            stat_names,
            [
                "hp",
                "attack",
                "defense",
                "special-attack",
                "special-defense",
                "speed",
                "accuracy",
                "evasion",
            ],
        )

    @mock.patch("random.randint", side_effect="1")
    def test_get_random_pokemon(self, mock_request):
        random_pokemon = get_random_pokemon()
        self.assertEqual(random_pokemon["name"], "bulbasaur")
        return random_pokemon

    @mock.patch("requests.get", side_effect=mocked_pokemon_requests_get)
    # @mock.patch("random.randint", side_effect="1")
    def test_convert_json_to_pokemon(self, mock_response):
        pokemon_obj = convert_json_to_pokemon()
        # expected_value = Pokemon(name="bulbasaur", stats=[Statistic[]])
        self.assertEqual(pokemon_obj, "asd")
