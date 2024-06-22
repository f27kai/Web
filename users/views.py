from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from . import forms, models, middlewares



class RegistrationView(CreateView):
    form_class = forms.CustomRegistrationForm
    template_name = "users/register.html"
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        response = super().form_valid(form)
        specialty = form.cleaned_data["specialty"]
        if specialty == "Java":
            self.object.club = "Java Club"
        elif specialty == "Python":
            self.object.club = "Python Club"
        elif specialty == "JS":
            self.object.club = "JavaScript Club"
        elif specialty == "C++":
            self.object.club = "C++ Club"
        elif specialty == "C#":
            self.object.club = "C# Club"
        elif specialty == "UX/UI Design":
            self.object.club = "UX/UI Design Club"
        else:
            self.object.club = "Клуб не определен"
        self.object.save()
        return response



class AuthLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = "users/login.html"

    def get_success_url(self):
        return reverse("users:user_list")



class AuthLogoutView(LogoutView):
    next_page = reverse_lazy("users:login")


class UserListView(ListView):
    template_name = "users/user_list.html"
    model = models.CustomUser

    def get_queryset(self):
        return models.CustomUser.objects.filter().order_by("-id")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["club"] = getattr(self.request, "club", "Клуб не определен")
        return context

