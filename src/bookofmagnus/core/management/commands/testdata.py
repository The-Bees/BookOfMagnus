import pandas
import xlrd

from django.core.management.base import BaseCommand, CommandError
from core.models import Book, Affiliation, Character

test_data = [
    {"title": "Horus Rising", "follows": []},
    {"title": "False Gods", "follows": ["Horus Rising"]},
    {"title": "Galaxy In Flames", "follows": ["False Gods"]},
    {"title": "Flight of the Eisenstein", "follows": ["Galaxy In Flames"]},
    {"title": "After Desh'ea", "follows": ["Galaxy In Flames"]},
    {"title": "Mechanicum", "follows": ["Galaxy In Flames"]},
    {"title": "The Last Church", "follows": ["Flight of the Eisenstein"]},
    {"title": "Fulgrim", "follows": ["Flight of the Eisenstein"]}
]

legions = [
    "Sons of Horus",
    "Imperial Fists",
    "Blood Angels",
    "World Eaters",
    "Emperor's Children",
    "Death Guard",
    "Iron Hands",
    "Salamanders",
    "Raven Guard",
    "Dark Angels",
    "Alpha Legion",
    "Thousand Sons",
    "Space Wolves",
    "Word Bearers",
    "Ultramarines",
    "Night Lords",
    "Iron Warriors",
    "White Scars",
]


class Command(BaseCommand):
    help = 'Adds test data to the db'

    # def add_arguments(self, parser):
    #     parser.add_argument('poll_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        Book.objects.all().delete()
        Affiliation.objects.all().delete()
        Character.objects.all().delete()


        # Add the books

        books_df = pandas.read_excel('books.xlsx')

        for index, row in books_df.iterrows():

            book = Book.objects.create(
                title=row['Title'],
                type=row['Format'].upper()
            )

        # Create the legions
        for legion in legions:

            Affiliation.objects.create(
                name=legion,
                legion=True
            )

        characters_df = pandas.read_excel('characters.xlsx')

        # Add the characters
        for index, row in characters_df.iterrows():

            print(row["Type"], row["Name"])

            if row["Type"]:
                affiliation, created = Affiliation.objects.get_or_create(name=row["Affiliation"])

                character = Character.objects.create(
                    name=row["Name"],
                    type=row["Type"].upper(),

                )

                character.affiliation.add(affiliation.id)


