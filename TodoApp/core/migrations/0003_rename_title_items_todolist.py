# Generated by Django 4.1 on 2023-05-31 09:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_todolist_items_items'),
    ]

    operations = [
        migrations.RenameField(
            model_name='items',
            old_name='title',
            new_name='todolist',
        ),
    ]
