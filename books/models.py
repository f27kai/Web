from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models



class Age_Books(models.Model):
    types = models.CharField(max_length=120, null=True)

    def __str__(self):
        return self.types

    class Meta:
        verbose_name = "Книга по возрастам"
        verbose_name_plural = "Книги по возрастам"


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
    age_books = models.ManyToManyField(Age_Books, null=True)


    def __str__(self):
        return f"{self.title} - {self.author}"
    class Meta:
        verbose_name = "Книг"
        verbose_name_plural = "Книги"


class Comment_books(models.Model):
    reviews_books = models.ForeignKey(Books, on_delete=models.CASCADE, related_name="review_books")
    text = models.TextField()
    stars = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.stars} - {self.reviews_books}"

    class Meta:
        verbose_name = "Комментарий книг"
        verbose_name_plural = "Комментарии книги"