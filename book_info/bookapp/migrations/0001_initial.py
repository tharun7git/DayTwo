# Generated by Django 5.0.6 on 2024-06-26 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Book",
            fields=[
                ("Bookid", models.AutoField(primary_key=True, serialize=False)),
                ("Bookname", models.CharField(max_length=200)),
                ("Author", models.CharField(max_length=200)),
                ("Rack", models.CharField(max_length=10)),
            ],
        ),
    ]