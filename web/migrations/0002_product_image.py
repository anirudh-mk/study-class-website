# Generated by Django 5.0.7 on 2024-07-12 04:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("web", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="image",
            field=models.ImageField(default=1, upload_to="media"),
            preserve_default=False,
        ),
    ]
