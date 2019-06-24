# Generated by Django 2.2.2 on 2019-06-24 21:08

from django.db import migrations

def book_data(apps, schema_editor):
    
    Book = apps.get_model('shelfapp', 'Book')
    for book in Book.objects.all():
        book.title = '%s %s' % (person.first_name, person.last_name)
        book.save()

class Migration(migrations.Migration):

    dependencies = [
        ('shelfapp', '0002_auto_20190624_1655'),
    ]

    operations = [
        migrations.RunPython(combine_names),
    ]

class Migration(migrations.Migration):

    dependencies = [
        ('shelfapp', '0002_auto_20190624_1655'),
    ]

    operations = [
    ]