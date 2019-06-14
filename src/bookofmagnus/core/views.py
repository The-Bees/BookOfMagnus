from django.shortcuts import render
from django.http import HttpResponse
from pygraphviz import *

from core.models import Book, Character

# Create your views here.

def index(request):

    characters = Character.objects.all()

    graph = AGraph(directed=True)

    if request.method == "POST":
        character = request.POST.get("character")
        # FIXME: CHaracter is none or we want all charcters again

        books = Book.objects.filter(characters__name=character)

        # Get the books they follow on from
        prequels = get_prequels(books)

        # Remove any prequels already in books
        prequels = prequels.exclude(id__in=books)

        # Draw all the nodes
        for book in books:
            graph.add_node(book.id, label=book.title)

            if book.follows.exists():
                for parent in book.follows.all():
                    graph.add_edge(parent.id, book.id)

        for book in prequels:
            graph.add_node(book.id, label=book.title, shape="box", color="red")

            if book.follows.exists():
                for parent in book.follows.all():
                    graph.add_edge(parent.id, book.id)

    else:

        books = Book.objects.all()

        for book in books:
            graph.add_node(book.id, label=book.title)

            if book.follows.exists():
                for parent in book.follows.all():
                    graph.add_edge(parent.id, book.id)

    graph.layout(prog='dot')
    #print(graph.string())
    svg_graph = graph.draw(format="svg")

    context = {
        "svg": svg_graph,
        "characters": characters

    }


    return render(request, 'core/index.html', context)


def get_prequels(books):
    """
    Get all prequels recursively for a queryset of books
    """

    def _get_prequels(books):

        prequels = Book.objects.none()
        for book in books:

            if book.follows.exists():

                book_follows = book.follows.all()

                # Add them to the prequels queryset
                prequels |= book_follows

                # See if they have any prequels
                prequels |= _get_prequels(book_follows)

        return prequels

    prequels = _get_prequels(books)

    return prequels
