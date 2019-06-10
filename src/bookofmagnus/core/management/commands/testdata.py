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

            # Add and books they follow on from
            if type(row['Follows']) == str:
                follows_list = row['Follows'].split(",")

                for fbook in follows_list:
                    book.follows.add(Book.objects.get(title=fbook).id)

        # Create the legions
        for legion in legions:

            Affiliation.objects.create(
                name=legion,
                legion=True
            )

        characters_df = pandas.read_excel('characters.xlsx')

        # Add the characters
        for index, row in characters_df.iterrows():

            if row["Type"]:
                affiliation, created = Affiliation.objects.get_or_create(name=row["Affiliation"])

                character = Character.objects.create(
                    name=row["Name"],
                    type=row["Type"].upper(),

                )

                character.affiliation.add(affiliation.id)

                # Add them to any books they're in
                if type(row['Books']) == str:
                    books_list = row['Books'].split(",")
                    print(books_list)

                    for title in books_list:
                        print(title)
                        try:
                            book_obj = Book.objects.get(title=title)
                            book_obj.characters.add(character.id)
                        except:
                            # If book doesn't exist
                            pass


