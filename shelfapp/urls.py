from django.urls import path
from . import views


urlpatterns = [
     path('', views.index, name='index'),
     path('books/', views.BookListView.as_view(), name='books'),
     path('categories/', views.category, name="categories"),
     path('categories/<int:category_pk>', views.list_of_books_by_category, name="category-list"),

]