# Generated by Django 4.1 on 2023-05-31 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_rename_title_items_todolist'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='items',
            field=models.TextField(default='', max_length=300),
        ),
        migrations.DeleteModel(
            name='Items',
        ),
    ]
