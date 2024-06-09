from django.db import models

class Books(models.Model):
    BOOKS_GENRE = (
        ('history', 'История'),
        ('mystery', 'Детектив'),
        ('biography', 'Биография'),
        ('self-help', 'Саморазвитие'),
        ('fiction', 'Художественная литература')
    )


    img = models.ImageField(upload_to='images/', null=True)
    title = models.CharField(max_length=200, null=True)
    author = models.CharField(max_length=200, null=True)
    email = models.EmailField(default="@gmail.com", null=True)
    text = models.TextField(null=True)
    publish_date = models.DateField(null=True)
    genre = models.CharField(max_length=20, choices=BOOKS_GENRE, null=True)
    created_books = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return f"{self.title} - {self.author}"
    class Meta:
        verbose_name = "Книг"
        verbose_name_plural = "Книги"
