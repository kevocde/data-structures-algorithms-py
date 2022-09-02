"""
El patrón de diseño Adapter, permite la comunicación entre partes diferentes del sistema, traduciendo en caso de ser
necesario, la información suministrada por un servicio a otro.

Ejemplo:
    A continuación en un sistema se está consumiendo un API de pokemones y se requiere almacenar esta información en dos
    formatos diferentes, el primero en json y el segundo en xml, el API devuelve los datos en formato JSON, así que
    se necesitará un adaptador para poder traducir esta información.
"""
import requests

from dict2xml import dict2xml


class PokemonAPI:
    API_URL = 'https://pokeapi.co/api/v2'
    PAGINATOR_LIMIT = 20

    def get_all(self, offset: int = 0, limit: int = PAGINATOR_LIMIT) -> dict:
        """Retorna los datos de todos los pokemones conocidos hasta el momento"""
        response = requests.get(self.API_URL + '/pokemon', params={'offset': offset, 'limit': limit})

        return response.json() if response.status_code == 200 else {}

    def get_pokemon(self, name: str) -> dict:
        """Retorna la información detallada de un pokemon por medio de su nombre """
        response = requests.get(f'{self.API_URL}/pokemon/{name}')

        return response.json() if response.status_code == 200 else {}


class PokemonAPIAdapter:
    def __init__(self, pokemonapi_inst: PokemonAPI):
        self._pokemonAPI = pokemonapi_inst

    def get_all_to_xml(self, offset: int = 0, limit: int = PokemonAPI.PAGINATOR_LIMIT):
        return dict2xml(self._pokemonAPI.get_all(offset, limit))


if __name__ == '__main__':
    pokemonAPI = PokemonAPI()

    print("The client needs all pokemons:")
    print(pokemonAPI.get_all())

    pokemonAPIAdapter = PokemonAPIAdapter(pokemonAPI)

    print("The client needs all pokemons but in json format")
    print(pokemonAPIAdapter.get_all_to_xml())
