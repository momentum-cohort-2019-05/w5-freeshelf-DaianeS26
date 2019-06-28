from django.urls import path
from . import views

urlpatterns = [
     path('', views.index, name='index'),
     path('books/', views.BookListView.as_view(), name='books'),
     path('categories/', views.category, name="categories"),
     # path('', views.CategoryDetailView.as_view(), name='category-detail'),

]