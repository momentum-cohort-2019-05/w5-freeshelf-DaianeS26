from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    """Model representing a book category."""
    name = models.CharField(max_length=200, help_text='Enter a book genre (e.g. Science Fiction)')
    
    class Meta:
        verbose_name_plural = "categories"
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('category-detail', args=[str(self.id)])
        
    def __str__(self):
        """String for representing the Model object."""
        return self.name


class Book(models.Model):
    """Model representing a book"""

    title = models.CharField(max_length=100)
    author = models.CharField(max_length = 100)
    description = models.CharField(max_length = 500)
    url = models.URLField(max_length = 200, unique=True)
    date_added = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category, help_text='Select a category for this book')

    class Meta: 
        ordering = ['-date_added']

    
    def __str__(self):
        """String for representing the Model object."""
        return self.title
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('book-detail', args=[str(self.id)])

    def display_category(self):
        """Create a string for the Category. This is required to display genre in Admin."""
        return ', '.join(category.name for category in self.category.all()[:3])
    
    display_category.short_description = 'Category'

class Favorite(models.Model):
   user = models.ForeignKey(User, unique=False, on_delete=models.CASCADE)
   book = models.ForeignKey(Book, unique=False, on_delete=models.CASCADE)

