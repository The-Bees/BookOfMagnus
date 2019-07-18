import json

from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, JsonResponse

from core.models import Book


def book(request, book_id):
    """
    Book api
    """

    try:
        book = Book.objects.get(id=book_id)

        response = {
            "title": book.title,
            "type": book.type,
            "author": book.author,
            "blurb": book.blurb,
            "series_no": book.series_no,
            "primary_characters": [character.name for character in book.primary_characters.all()],
            "follows": [follow.title for follow in book.follows.all()],
            "precedes": get_precedes(book),
            "factions": get_factions(book)
        }

        return JsonResponse(response)

    except ObjectDoesNotExist:
        return HttpResponse(status=404)


def get_precedes(book):
    precedes = Book.objects.filter(follows__in=[book])
    return [pre_book.title for pre_book in precedes]


def get_factions(book):

    # Set created to avoid duplicates
    factions = set()
    characters = book.primary_characters.all()

    for character in characters:
        factions.add(character.affiliation.name)

    return list(factions)
