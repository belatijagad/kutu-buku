from django.shortcuts import render
from halaman_buku.models import Book
# Create your views here.

def pencarian_buku(request):
    books = Book.objects.all()
    categories = Book.objects.values_list('Category', flat=True).distinct()
    return render(request, 'pencarian_buku.html', {'books':books, 'categories':categories})

def cari_buku(request):
    categories = Book.objects.values_list('Category', flat=True).distinct()
    query = request.GET.get('query')
    selected_category = request.GET.get('Category', '')
    urutan_rating = request.GET.get('urutan_rating', 'ratingTertinggi')

    if query and selected_category:
        books = Book.objects.filter(Title__icontains=query, Category=selected_category)
    elif query:
        books = Book.objects.filter(Title__icontains=query)
    elif selected_category:
        books = Book.objects.filter(Category=selected_category)
    else:
        books = Book.objects.all()

    if urutan_rating == "ratingTertinggi":
        books = books.order_by('-Rating')
    else:
        books = books.order_by('Rating')
    return render(request, 'pencarian_buku.html', {'books':books, 'categories':categories, 'selected_category':selected_category})

