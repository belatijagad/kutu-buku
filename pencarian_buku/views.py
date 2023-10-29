from django.shortcuts import render
from django.http import JsonResponse
from halaman_buku.models import Book
# Create your views here.

def pencarian_buku(request):
    books = Book.objects.all()

    context = {
        'books': books,
    }
    return render(request, 'pencarian_buku.html', context)

def search_all(request):
    query = request.GET.get('q', '')
    sort_option = request.GET.get('sort', 'rating')
    direction = request.GET.get('direction', 'desc')
    genre_slug = request.GET.get('genre', '')

    if not query.strip():
        results = Book.objects.all()
    else:
        results = Book.objects.filter(title__icontains=query)

    if genre_slug:
        results = results.filter(genre__icontains=genre_slug)

    order_prefix = '' if direction == 'asc' else '-'

    if sort_option == "rating":
        results = results.order_by(order_prefix+'score')
    elif sort_option == "popularity":
        results = results.order_by(order_prefix+'reviewers')
    elif sort_option == "alfabet":
        results = results.order_by(order_prefix+'title')

    data = [{
        'id': book.id,
        'title': book.title,
        'author': book.author,
        'img_src': book.img_src,
        'genre': book.genre,
        'synopsis': book.synopsis,
        'reviewers': book.reviewers,
        'chapters': book.chapters,
        'score': book.score,
        'published_at': book.published_at.strftime('%Y-%m-%d')  # Date to string
    } for book in results]
    return JsonResponse(data, safe=False)