from django.shortcuts import render
from django.http import HttpResponseRedirect
from tambah_buku.forms import NovelForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login/')
def create_novel(request):
    form = NovelForm(request.POST or None)

    if form.is_valid() and request.method == 'POST':
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))
    
    context = {'form': form}

    return render(request, 'tambah_buku.html', context)
