from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import datetime
import random
from . import models




def all_books_age_view(request):
    if request.method == "GET":
        all_books_age = models.Books.objects.filter().order_by("-id")
        return render(
            request,
            template_name='age_books/all_books_age.html',
            context={
                "all_books_age": all_books_age
            }
        )


def children(request):
    if request.method == "GET":
        childrens = models.Books.objects.filter(age_books__types = "Книги для детей").order_by("-id")
        return render(
            request,
            template_name="age_books/children.html",
            context={
                'childrens': childrens
            }
        )

def teenage(request):
    if request.method == "GET":
        teenages = models.Books.objects.filter(age_books__types="Книги для подростков").order_by("-id")
        return render(
            request,
            template_name="age_books/teenage.html",
            context={
                "teenages": teenages
            }
        )


def adults(request):
    if request.method == "GET":
        adults = models.Books.objects.filter(age_books__types="Книги для взрослых").order_by("-id")
        return render(
            request,
            template_name="age_books/adults.html",
            context={
                "adults": adults
            }
        )

def book_list_view(request):
    if request.method == "GET":
        books = models.Books.objects.filter().order_by("-id")
        return render(
            request,
            template_name="books/books_list.html",
            context={
                "books": books
            }
        )


def books_detail_view(request, id):
    if request.method == "GET":
        books_id = get_object_or_404(models.Books, id=id)
        return render(
            request,
            template_name="books/books_detail.html",
            context={
                "books_id": books_id
            }
        )

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