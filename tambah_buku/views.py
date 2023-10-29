from django.shortcuts import render, redirect
from .forms import BookForm

def add_book(request):
    if not request.user.is_authenticated:
        return redirect('login')  # Redirect ke halaman login jika pengguna belum masuk.

    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # Ganti 'book_list' dengan nama URL daftar buku.

    else:
        form = BookForm()

    return render(request, 'add_book.html', {'form': form})
