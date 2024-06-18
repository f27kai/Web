from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views import generic
import datetime
import random
from . import models
from .forms import BooksForm


class Search_books(generic.ListView):
    template_name = "books/books_list.html"
    context_object_name = "books"
    paginate_by = 5

    def get_queryset(self):
        return models.Books.objects.filter(title__icontains = self.request.GET.get('q')).order_by("-id")


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context
# Update
class Update_book_view(generic.UpdateView):
    template_name = "crud_books/update_books.html"
    form_class = BooksForm
    success_url = '/books_list/'

    def get_object(self, **kwargs):
        book_id = self.kwargs.get('id')
        return get_object_or_404(models.Books, id=book_id)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(Update_book_view, self).form_valid(form=form)


# def update_book_view(request, id):
#     update_book = get_object_or_404(models.Books, id=id)
#
#     if request.method == "POST":
#         form = BooksForm(request.POST, instance=update_book)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('<h3>Книга успешно изменена!</h3>'
#                                 '<a href="/books_list/">Список книг</a>')
#     else:
#         form = BooksForm(instance=update_book)
#
#     return render(
#         request,
#         template_name="crud_books/update_books.html",
#         context={
#             "form": form,
#             "update_book": update_book
#         }
#     )




# Delete
class Delete_books_view(generic.DeleteView):
    template_name = "crud_books/delete_book"
    success_url = '/books_list/'

    def get_object(self, **kwargs):
        book_id = self.kwargs.get("id")
        return get_object_or_404(models.Books, id=book_id)

# def delete_books_view(request, id):
#     book_id = get_object_or_404(models.Books, id=id)
#     book_id.delete()
#     return HttpResponse('<h3>Книга успешно удалено!</h3>'
#                         '<a href="/books_list/">Список книг</a>')




# Create
class Create_books_view(generic.CreateView):
    template_name = "crud_books/create_books.html"
    form_class = BooksForm
    success_url = '/books_list/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(Create_books_view, self).form_valid(form=form)


# def create_books_view(request):
#     if request.method == "POST":
#         form = BooksForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('<h3>Книга успешно добавлена!</h3>'
#                                 '<a href="/books_list/">Список книг</a>')
#
#     else:
#         form = BooksForm()
#
#     return render(
#         request,
#         template_name="crud_books/create_books.html",
#         context={
#             "form": form
#         }
#     )





# Info
class All_books_age_view(generic.ListView):
    template_name = "age_books/all_books_age.html"
    context_object_name = "all_books_age"
    model = models.Books

    def get_queryset(self):
        return self.model.objects.filter().order_by("-id")

# def all_books_age_view(request):
#     if request.method == "GET":
#         all_books_age = models.Books.objects.filter().order_by("-id")
#         return render(
#             request,
#             template_name='age_books/all_books_age.html',
#             context={
#                 "all_books_age": all_books_age
#             }
#         )


class Children(generic.ListView):
    template_name = "age_books/children.html"
    context_object_name = "childrens"
    model = models.Books

    def get_queryset(self):
        return self.model.objects.filter(age_books__types = "Книги для детей").order_by("-id")

# def children(request):
#     if request.method == "GET":
#         childrens = models.Books.objects.filter(age_books__types = "Книги для детей").order_by("-id")
#         return render(
#             request,
#             template_name="age_books/children.html",
#             context={
#                 'childrens': childrens
#             }
#         )



class Teenage(generic.ListView):
    template_name = "age_books/teenage.html"
    context_object_name = "teenages"
    model = models.Books

    def get_queryset(self):
        return self.model.objects.filter(age_books__types="Книги для подростков").order_by("-id")

# def teenage(request):
#     if request.method == "GET":
#         teenages = models.Books.objects.filter(age_books__types="Книги для подростков").order_by("-id")
#         return render(
#             request,
#             template_name="age_books/teenage.html",
#             context={
#                 "teenages": teenages
#             }
#         )



class Adults(generic.ListView):
    template_name = "age_books/adults.html"
    context_object_name = "adults"
    model = models.Books

    def get_queryset(self):
        return self.model.objects.filter(age_books__types="Книги для взрослых").order_by("-id")

# def adults(request):
#     if request.method == "GET":
#         adults = models.Books.objects.filter(age_books__types="Книги для взрослых").order_by("-id")
#         return render(
#             request,
#             template_name="age_books/adults.html",
#             context={
#                 "adults": adults
#             }
#         )


class Books_detail_view(generic.DetailView):
    template_name = "books/books_detail.html"
    context_object_name = "books_id"

    def get_object(self, **kwargs):
        books_id = self.kwargs.get('id')
        return get_object_or_404(models.Books, id = books_id)



# def books_detail_view(request, id):
#     if request.method == "GET":
#         books_id = get_object_or_404(models.Books, id=id)
#         return render(
#             request,
#             template_name="books/books_detail.html",
#             context={
#                 "books_id": books_id
#             }
#         )



class Book_list_view(generic.ListView):
    template_name = "books/books_list.html"
    context_object_name = "books"
    model = models.Books

    def get_queryset(self):
        return self.model.objects.filter().order_by('-id')

# def book_list_view(request):
#     if request.method == "GET":
#         books = models.Books.objects.filter().order_by("-id")
#         return render(
#             request,
#             template_name="books/books_list.html",
#             context={
#                 "books": books
#             }
#         )

def name_surname_view(request):
    if request.method == "GET":
        return HttpResponse("Кайратбекова Феруза 21 лет")

def hobby_view(request):
    if request.method == "GET":
        return HttpResponse("My hobbies include dancing, "
                            "coding, and sleeping. "
                            "I enjoy dancing because it allows me to express myself creatively and stay physically active."
                            " Coding is another passion of mine; I love solving problems and building projects through programming. "
                            "Additionally, I value my sleep, as it helps me recharge and maintain a healthy lifestyle.")



def get_datetime_view(request):
    if request.method == "GET":
        current_date_time = datetime.datetime.now()
        current_time = current_date_time.time()
        return HttpResponse(f"Часы: {current_time}")


def random_number_view(request):
    if request.method == "GET":
        return HttpResponse(random.randint(1, 1000))