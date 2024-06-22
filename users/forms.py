from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models
from django.db.models.signals import post_save
from django.dispatch import receiver

GENDER = (("Male", "Male"), ("Female", "Female"))

class CustomRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True)
    age = forms.IntegerField(required=True)
    gender = forms.ChoiceField(choices=GENDER, required=True)
    specialty = forms.ChoiceField(choices=models.CustomUser.SPECIALTIES, required=True)

    class Meta:
        model = models.CustomUser
        fields = (
            "username",
            "email",
            "password1",
            "password2",
            "first_name",
            "last_name",
            "age",
            "gender",
            "phone_number",
            "specialty",
        )

    def save(self, commit=True):
        user = super(CustomRegistrationForm, self).save(commit=True)
        user.email = self.cleaned_data["email"]
        user.save()

        user.specialty = self.cleaned_data["specialty"]
        if commit:
            user.save()
        return user

@receiver(post_save, sender=models.CustomUser)
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
