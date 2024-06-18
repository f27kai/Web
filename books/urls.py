from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('search/', views.Search_books.as_view(), name='search'),

    path('create_books/', views.Create_books_view.as_view(), name="create_books"),
    path('books/<int:id>/', views.Delete_books_view.as_view(), name="delete_books"),
    path('books_update/<int:id>/', views.Update_book_view.as_view(), name="update_book"),

    path('all_books_age/', views.All_books_age_view.as_view()),
    path('children/', views.Children.as_view()),
    path('teenage/', views.Teenage.as_view()),
    path('adults/', views.Adults.as_view()),
    path("books_list/", views.Book_list_view.as_view(), name='book_list'),
    path('book/<int:id>/', views.Books_detail_view.as_view(), name='book_detail'),
    path("name/", views.name_surname_view),
    path("hobby/", views.hobby_view),
    path("datetime/", views.get_datetime_view),
    path("number/", views.random_number_view),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)