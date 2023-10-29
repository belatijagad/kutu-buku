from django.forms import ModelForm
from halaman_buku.models import Book

class NovelForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'chapters', 'img_src', 'synopsis', 'reviewers', 'score', 'genre']

