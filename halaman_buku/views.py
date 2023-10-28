from django.shortcuts import render, redirect
from .models import Book, Ulasan
from .forms import ReviewForm

#Create your views here
def buku_detail(request, book_id):
    book = Book.objects.get(pk=book_id)
    ulasan = Ulasan.objects.filter(book=book)
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            ulasan = form.save(commit=False)
            ulasan.user = request.user
            ulasan.book = book
            ulasan.save()
            return redirect('buku_detail', book_id=book_id)
    else:
        form = ReviewForm()
    
    context = {'book': book, 'ulasan': ulasan, 'form': form}
    return render(request, 'ulasan.html', context)
