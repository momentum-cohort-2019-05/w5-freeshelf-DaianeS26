# Generated by Django 2.2.2 on 2019-06-29 16:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shelfapp', '0005_auto_20190628_1743'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='categories',
            new_name='category',
        ),
    ]
