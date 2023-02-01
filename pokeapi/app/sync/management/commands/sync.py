from typing import (
    Tuple,
    Dict,
)
from django.core.management.base import (
    BaseCommand,
)
from app.pokeapi.models import Berry
from app.helpers import get_data


class Command(BaseCommand):
    help = "Poke Api migrator Tool"

    def handle(self, *args: Tuple, **options: Dict) -> None:
        if Berry.objects.count() > 0:
            print("Nothing to do!")
            return

        query = """
        query PokeAPIChallenge {
            berries: pokemon_v2_berry {
                id
                name
                growth_time
            }
        }"""
        response = get_data(query)
        records = [
            Berry(name=item["name"], growth_time=item["growth_time"])
            for item in response
        ]
        Berry.objects.bulk_create(records)
        print("Migrated!")
