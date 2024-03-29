from django.contrib.auth.decorators import login_required
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.shortcuts import render
from django.http import HttpResponse
from pygraphviz import *

from core.models import Affiliation, Book, Character


@login_required()
def index(request):

    characters = Character.objects.all()
    affiliations = Affiliation.objects.all()

    graph = AGraph(directed=True, bgcolor="transparent")

    if request.method == "POST":
        character = request.POST.get("character")
        affiliation = request.POST.get("affiliation")

        if character:
            books = Book.objects.filter(characters__name=character)
        elif affiliation:
            affiliation_obj = Affiliation.objects.get(name=affiliation)
            books = Book.objects.filter(characters__affiliation__in=[affiliation_obj])
        else:
            books = Book.objects.all()

        # Get the books they follow on from
        prequels = get_prequels(books)

        # Remove any prequels already in books
        prequels = prequels.exclude(id__in=books)

        # Draw all the nodes
        for book in books:
            graph.add_node(book.id, id="main-book-{}".format(book.id), label=book.title)

            if book.follows.exists():
                for parent in book.follows.all():
                    graph.add_edge(parent.id, book.id)

        for book in prequels:
            graph.add_node(book.id, id="recommended-book-{}".format(book.id), label=book.title)

            if book.follows.exists():
                for parent in book.follows.all():
                    graph.add_edge(parent.id, book.id)

    else:

        books = Book.objects.all()

        for book in books:
            graph.add_node(book.id, id="main-book-{}".format(book.id), label=book.title)

            if book.follows.exists():
                for parent in book.follows.all():
                    graph.add_edge(parent.id, book.id)

    #graph.graph_attr["splines"] = "curved"
    graph.edge_attr["arrowhead"] = "open"
    graph.node_attr["shape"] = "box"
    graph.layout(prog='dot')
    #print(graph.string())
    svg_graph = graph.draw(format="svg").decode("utf-8")

    context = {
        "svg": svg_graph,
        "characters": characters,
        "affiliations": affiliations
    }

    return render(request, 'core/index.html', context)


def get_prequels(books):
    """
    Get all prequels recursively for a queryset of books
    """

    prequels = Book.objects.none()

    for book in books:

        if book.follows.exists():

            book_follows = book.follows.all()

            # Add them to the prequels queryset
            prequels |= book_follows

            # See if they have any prequels
            prequels |= get_prequels(book_follows)

    return prequels


