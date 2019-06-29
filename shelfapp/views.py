from django.shortcuts import render
from .models import Book, Category, Favorite
from django.views import generic
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

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


class CategoryDetailView(generic.DetailView):
    model = Category

@login_required
def user_favorites(request):
   favorites = Favorite.objects.filter(user=request.user)

   favorites_list = []

   for favorite in favorites:
       favorites_list.append(favorite.book)

   context = {
       'favorites': favorites,
       'favorites_list': favorites_list,
   }

   return render(request, 'shelfapp/added_favorites.html', context)


@login_required
def add_to_favorites(request, pk):
    book = get_object_or_404(Book, pk=pk)

    new_favorite, created = Favorite.objects.get_or_create(book=book, user=request.user)
    
    if not created:
        new_favorite.delete()

        context = {
        'book': book,
        'new_favorite': new_favorite,
        'created': created,
        }

    return render(request, 'shelfapp/favorite_added.html', context)