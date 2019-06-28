from django.urls import path
from . import views

urlpatterns = [
     path('', views.index, name='index'),
     path('books/', views.BookListView.as_view(), name='books'),
     # path('<int:pk>', views.CategoryDetailView.as_view(), name='category-detail'),

]