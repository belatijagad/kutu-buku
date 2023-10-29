# Generated by Django 4.2.4 on 2023-10-28 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
    ]