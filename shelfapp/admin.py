from django.contrib import admin
from shelfapp.models import Book, Category

# Register your models here.

# admin.site.register(Book)
admin.site.register(Category)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_added', 'display_category')