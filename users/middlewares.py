from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseBadRequest


class SpecialtyClubMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path == "/register/" and request.method == "POST":
            specialty = request.POST.get("specialty")
            if not specialty:
                return HttpResponseBadRequest("Специальность не указана")

            if specialty == "Java":
                request.club = "Java Club"
            elif specialty == "Python":
                request.club = "Python Club"
            elif specialty == "JS":
                request.club = "JavaScript Club"
            elif specialty == "C++":
                request.club = "C++ Club"
            elif specialty == "C#":
                request.club = "C# Club"
            elif specialty == "UX/UI Design":
                request.club = "UX/UI Design Club"
            else:
                return HttpResponseBadRequest("Неверная специальность")

        elif request.path == "/register/" and request.method == "GET":
            setattr(request, "club", "Клуб не определен")
