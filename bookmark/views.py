from django.shortcuts import render
from .forms import SearchForm
from halaman_buku.models import Book
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required

def show_json_by_id(request, id):
    data = Book.objects.filter(pk=id)
    return HttpResponse (serializers.serialize("json", data), content_type="application/json")

@login_required(login_url='/login')
def show_main(request):
    context = {
        'novels': Book.objects.all(),
        'jumlah': Book.objects.count(),
    }
    return render(request, 'daftar_membaca.html', context)

def search(request):
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