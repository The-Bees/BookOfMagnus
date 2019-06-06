from django.core.management.base import BaseCommand, CommandError
from core.models import Book

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


class Command(BaseCommand):
    help = 'Adds test data to the db'

    # def add_arguments(self, parser):
    #     parser.add_argument('poll_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        Book.objects.all().delete()
        for data in test_data:
            book = Book.objects.create(
                title=data["title"]
            )
            if data["follows"]:
                for parent in data["follows"]:
                    book.follows.add(Book.objects.get(title=parent))
