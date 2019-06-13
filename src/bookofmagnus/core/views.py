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
        # might need a function that grabs books all the way back, recursively
        # To begin with show these in a different shape - perhaps a square
        #follow_books

    else:

        books = Book.objects.all()

        for book in books:
            graph.add_node(book.id, label=book.title)

            if book.follows:
                for parent in book.follows.all():
                    graph.add_edge(parent.id, book.id)

    graph.layout(prog='dot')
    svg_graph = graph.draw(format="svg")

    context = {
        "svg": svg_graph,
        "characters": characters

    }


    return render(request, 'core/index.html', context)


"""
def index(request):

    books = Book.objects.all()

    dot = Digraph(format="svg")
    for book in books:
        dot.node(book.strid(), label='''<<TABLE><TR><TD><img src="#"/></TD></TR></TABLE>>''')

        if book.follows:
            for parent in book.follows.all():
                dot.edge(parent.strid(), book.strid())

    dot_svg = dot.pipe().decode('utf-8')

    context = {"svg": dot_svg}
    return render(request, 'core/index.html', context)
"""
