from django.urls import path
from .views import (
    get_all_books,
    get_detail_about_book,
    book_details_handler,
    all_books_handler,
)

urlpatterns = [
    path("books/", get_all_books),
    path("books/<int:book_id>/", get_detail_about_book),
    path("api/books/", all_books_handler),
    path("api/books/<int:book_id>/", book_details_handler),
]
