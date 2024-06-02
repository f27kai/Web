from django.shortcuts import render
from django.http import HttpResponse
import datetime
import random

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