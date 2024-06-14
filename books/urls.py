from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('create_books/', views.create_books_view, name="create_books"),
    path('books/<int:id>/', views.delete_books_view, name="delete_books"),
    path('books_update/<int:id>/', views.update_book_view, name="update_book"),

    path('all_books_age/', views.all_books_age_view),
    path('children/', views.children),
    path('teenage/', views.teenage),
    path('adults/', views.adults),
    path("books_list/", views.book_list_view, name='book_list'),
    path('book/<int:id>/', views.books_detail_view, name='book_detail'),
    path("name/", views.name_surname_view),
    path("hobby/", views.hobby_view),
    path("datetime/", views.get_datetime_view),
    path("number/", views.random_number_view),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)