from django.shortcuts import render
from django.http import HttpResponse
from pygraphviz import *

from core.models import Book

# Create your views here.

def index(request):

    books = Book.objects.all()

    graph = AGraph(directed=True)

    for book in books:
        graph.add_node(book.id, label=book.title)

        if book.follows:
            for parent in book.follows.all():
                graph.add_edge(parent.id, book.id)

    print(graph.string())

    graph.layout(prog='dot')
    svg_graph = graph.draw(format="svg")
    context = {"svg": svg_graph}
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
