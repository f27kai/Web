# Generated by Django 5.0.6 on 2024-06-07 14:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='books',
            options={'verbose_name': 'Книг', 'verbose_name_plural': 'Книги'},
        ),
        migrations.RemoveField(
            model_name='books',
            name='author',
        ),
        migrations.RemoveField(
            model_name='books',
            name='description',
        ),
        migrations.RemoveField(
            model_name='books',
            name='genre',
        ),
        migrations.RemoveField(
            model_name='books',
            name='publish_date',
        ),
        migrations.RemoveField(
            model_name='books',
            name='title',
        ),
    ]