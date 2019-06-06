from django.shortcuts import render
from django.http import HttpResponse
from pygraphviz import *

from core.models import Book

# Create your views here.

def index(request):

    books = Book.objects.all()

    graph = AGraph(directed=True)

    for book in books:
        graph.add_node(book.title)

        if book.follows:
            for parent in book.follows.all():
                graph.add_edge(parent.title, book.title)

    print(graph.string())

    graph.layout(prog='dot')
    graph.draw('file.png')
    context = {}
    return render(request, 'core/index.html', context)
