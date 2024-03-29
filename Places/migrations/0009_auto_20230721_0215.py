# Generated by Django 3.1.3 on 2023-07-20 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Places', '0008_restaurant_about'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='image_URL',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='place',
            name='image_URL',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='image_URL',
            field=models.URLField(blank=True),
        ),
    ]
