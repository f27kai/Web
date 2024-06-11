from django.contrib import admin
from . import models

admin.site.register(models.Books)
admin.site.register(models.Comment_books)
admin.site.register(models.Age_Books)
