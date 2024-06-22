from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.signals import post_save
from django.dispatch import receiver

class CustomUser(User):
    GENDER = (("Male", "Male"), ("Female", "Female"))

    SPECIALTIES = [
        ("Java", "Java"),
        ("Python", "Python"),
        ("JS", "JavaScript"),
        ("C++", "C++"),
        ("C#", "C#"),
        ("UX/UI Design", "UX/UI Design"),
    ]

    phone_number = models.CharField(max_length=14, default="+996")
    age = models.PositiveIntegerField(default=18, validators=[MaxValueValidator(60), MinValueValidator(14)])
    gender = models.CharField(max_length=100, choices=GENDER)
    specialty = models.CharField(max_length=50, choices=SPECIALTIES)
    club = models.CharField(max_length=50, default="Клуб не определен")

@receiver(post_save, sender=CustomUser)
def set_club(sender, instance, created, **kwargs):
    if created:
        print("Сигнал обработан успешно: пользователь зарегистрировался")
        specialty = instance.specialty
        if specialty == "Java":
            instance.club = "Java Club"
        elif specialty == "Python":
            instance.club = "Python Club"
        elif specialty == "JS":
            instance.club = "JavaScript Club"
        elif specialty == "C++":
            instance.club = "C++ Club"
        elif specialty == "C#":
            instance.club = "C# Club"
        elif specialty == "UX/UI Design":
            instance.club = "UX/UI Design Club"
        else:
            instance.club = "Клуб не определен"
        instance.save()

