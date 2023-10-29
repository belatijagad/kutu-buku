# Generated by Django 4.2.6 on 2023-10-28 15:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=255)),
                ('Category', models.CharField(max_length=100)),
                ('Image', models.URLField()),
                ('Rating', models.IntegerField()),
                ('Description', models.TextField(blank=True, null=True)),
                ('UPC', models.CharField(max_length=12, unique=True)),
                ('Product Type', models.CharField(default='Books', max_length=50)),
                ('Price (excl', models.DecimalField(decimal_places=2, max_digits=6)),
                ('Price (incl', models.DecimalField(decimal_places=2, max_digits=6)),
                ('Tax', models.DecimalField(decimal_places=2, max_digits=6)),
                ('Availability', models.CharField(max_length=50)),
                ('Number of reviews', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Ulasan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('comment', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='halaman_buku.book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
