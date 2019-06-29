from django.shortcuts import render
from .models import Book, Category
from django.views import generic
from django.http import HttpResponse

# Create your views here.


def index(request):
    """View function for home page of site."""

    list_of_books = Book.objects.all()
    list_of_categories = Category.objects.all()
    
    context = {
        'list_of_books': list_of_books,
        'list_of_categories': list_of_categories,
        
    }
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


class BookListView(generic.ListView):
    model = Book
    

def category(request):

    category_list = Category.objects.all()

    context = {
        'category_list': category_list,
    }

    return render(request, 'shelfapp/categories.html', context=context)


def list_of_books_by_category(request, category_pk):
  
    books_by_category = Book.objects.filter(categories__id=category_pk)

    context = {
        'books_by_category': books_by_category,

    }

    return render(request, 'shelfapp/categories_list.html', context=context)


