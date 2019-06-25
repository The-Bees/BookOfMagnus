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
            "blurb": book.blurb
        }

        return JsonResponse(response)

    except ObjectDoesNotExist:
        return HttpResponse(status=404)
