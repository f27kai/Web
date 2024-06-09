from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import datetime
import random
from . import models


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