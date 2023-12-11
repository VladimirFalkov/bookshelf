from django.http import (
    HttpRequest,
    HttpResponse,
    JsonResponse,
    HttpResponseNotFound,
)


from django.shortcuts import render, get_object_or_404
from .models import Book


def get_all_books(request: HttpRequest):
    books = Book.objects.all()
    return render(request, "all_books.html", context={"books": books})


def get_detail_about_book(request: HttpRequest, book_id: int):
    book = get_object_or_404(Book, id=book_id)
    return render(request, "detail_book.html", context={"book": book})


def book_details_handler(request: HttpRequest, book_id: int) -> HttpResponse:
    book = get_object_or_404(Book, id=book_id)

    if book is None:
        return HttpResponseNotFound()

    return JsonResponse(
        {
            "id": book.pk,
            "title": book.title,
            "author_full_name": book.author_full_name,
            "isbn": book.year_of_publishing,
            "copies_printed": book.copies_printed,
            "short_description": book.short_description,
        }
    )


def all_books_handler(request: HttpRequest) -> HttpResponse:
    books = list(Book.objects.values())

    return JsonResponse(books, safe=False)
