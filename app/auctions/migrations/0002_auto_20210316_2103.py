# Generated by Django 3.1.7 on 2021-03-16 21:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("auctions", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="listing",
            old_name="image_url",
            new_name="_image_url",
        ),
    ]
