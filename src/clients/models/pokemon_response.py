from typing import TypedDict


class PokemonResponse(TypedDict):
    id: str
    name: str
    category: str
    entry: str
    generation: int
    types: list[str]
    weaknesses: list[str]
    resistances: list[str]
    immunities: list[str]
