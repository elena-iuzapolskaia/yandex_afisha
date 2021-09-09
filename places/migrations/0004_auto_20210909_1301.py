# Generated by Django 3.2.7 on 2021-09-09 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_image_place'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='placeId',
            field=models.CharField(blank=True, max_length=200, verbose_name='Уникальный идентификатор локации'),
        ),
        migrations.AlterField(
            model_name='image',
            name='photo',
            field=models.ImageField(upload_to='media'),
        ),
    ]
