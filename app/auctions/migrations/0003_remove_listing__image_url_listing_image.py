# Generated by Django 4.0.4 on 2022-06-01 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_auto_20210316_2103'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='_image_url',
        ),
        migrations.AddField(
            model_name='listing',
            name='image',
            field=models.ImageField(null=True, upload_to='uploads/', verbose_name='Image'),
        ),
    ]
