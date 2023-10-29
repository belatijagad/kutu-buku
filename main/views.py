from django.shortcuts import render
from halaman_buku.models import Book

# Create your views here.
def show_main(request):
    return render(request, "main.html")