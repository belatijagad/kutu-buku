from django.shortcuts import render, redirect
from .models import Book, Ulasan
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

#Create your views here
def buku_detail(request, sha256sum):
    book = Book.objects.get(sha256sum=sha256sum)
    ulasan = Ulasan.objects.filter(book=book)

    if request.method == 'POST':
        tambah_ulasan(request, sha256sum=sha256sum)

    context = {'book': book, 'ulasan': ulasan}
    return render(request, 'ulasan.html', context)

@login_required(login_url='/login')
def tambah_ulasan(request, sha256sum):
    book = Book.objects.get(sha256sum=sha256sum)
    ulasan = Ulasan()
    ulasan.user = request.user
    ulasan.book = book
    ulasan.comment = request.POST['comment']
    ulasan.save()