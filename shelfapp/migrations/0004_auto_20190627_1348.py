# Generated by Django 2.2.2 on 2019-06-27 17:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shelfapp', '0003_auto_20190624_1708'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['-date_added']},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
    ]