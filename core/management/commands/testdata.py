import pandas
import xlrd

from django.core.management.base import BaseCommand, CommandError
from core.models import Book, Affiliation, Character


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

        characters_df = pandas.read_excel('characters.xlsx')

        # Add the characters
        for index, row in characters_df.iterrows():

            if row["Type"] and type(row["Name"]) == str:
                print("Adding character: {}".format(row["Name"]))
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

                        try:
                            book_obj = Book.objects.get(title=title)
                            book_obj.characters.add(character.id)
                        except:
                            # If book doesn't exist
                            pass


