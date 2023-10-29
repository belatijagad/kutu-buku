from django.shortcuts import render
from .forms import SearchForm
from halaman_buku.models import Book, Genre
from django.http import HttpResponse
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

def search_view(request):
    queryset = Book.objects.all()
    form = SearchForm(request.GET or None)

    if form.is_valid():
        query = form.cleaned_data.get('query')
        sort_by = form.cleaned_data.get('sort_by')

        if query:
            queryset = queryset.filter(name__icontains=query)

        if sort_by:
            queryset = queryset.order_by(sort_by)

    context = {
        'form': form,
        'queryset': queryset
    }

    return render(request, 'search_bar.html', context)