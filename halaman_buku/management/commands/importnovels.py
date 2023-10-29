from django.core.management.base import BaseCommand
import json
from django.core import serializers
from halaman_buku.models import Book, Genre

class Command(BaseCommand):
    help = 'Imports novels from a JSON file into the database'

    def handle(self, *args, **options):
        with open('utils/output/novels.json', 'r', encoding='utf-8') as file:
            data = json.load(file)

        for novel_data in data:
            # Extract genre names
            genre_names = novel_data.pop('genre', [])

            # Create or fetch related genres
            genres = [Genre.objects.get_or_create(name=genre_name)[0] for genre_name in genre_names]

            # print(novel_data['reviewers']);
            # break
            novel = Book()
            novel.title = novel_data['title']
            novel.author = novel_data['author']
            novel.chapters = novel_data['chapters']
            novel.img_src = novel_data['img_src']
            novel.synopsis = novel_data['synopsis']
            novel.reviewers = novel_data['reviewers']
            novel.score = novel_data['score']
            novel.save()

            for genre in genres:
                novel.genres.add(genre)

        self.stdout.write(self.style.SUCCESS('Successfully imported novels'))
