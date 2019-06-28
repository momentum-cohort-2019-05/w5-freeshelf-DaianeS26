from django.shortcuts import render
from .models import Book, Category
from django.views import generic
from django.http import HttpResponse

# Create your views here.


def index(request):
    """View function for home page of site."""

    book_list = Book.objects.all()
    category_list = Category.objects.all()
    
    context = {
        'book_list': book_list,
        'category_list': category_list,
        
    }
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


class BookListView(generic.ListView):
    model = Book
    

class CategoryDetailView(generic.DetailView):
    model = Category

def category(request):
    category_list = Category.objects.all()

    context = {
        'category_list': category_list,
    }


    return render(request, 'shelfapp/categories.html')