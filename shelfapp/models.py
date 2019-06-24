from django.db import models

# Create your models here.

class Category(models.Model):
    """Model representing a book genre."""
    name = models.CharField(max_length=200, help_text='Enter a book genre (e.g. Science Fiction)')
    
    class Meta:
        verbose_name_plural = "categories"
        
    def __str__(self):
        """String for representing the Model object."""
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length = 100)
    description = models.CharField(max_length = 500)
    url = models.URLField(max_length = 200, unique=True)
    date_added = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category, help_text='Select a category for this book')

    class Meta: 
        ordering = ['date_added']
    

    def __str__(self):
        """String for representing the Model object."""
        return self.title
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('book-detail', args=[str(self.id)])

