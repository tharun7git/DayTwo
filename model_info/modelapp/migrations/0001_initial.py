# Generated by Django 5.0.6 on 2024-06-30 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ModelU",
            fields=[
                ("user_id", models.AutoField(primary_key=True, serialize=False)),
                ("invoice_date", models.DateField()),
                ("job_card_date", models.DateField()),
                ("business_partner_name", models.CharField(max_length=200)),
                ("vehicle_no", models.IntegerField()),
                ("vehicle_model", models.CharField(max_length=200)),
                ("current_km_reading", models.IntegerField()),
                ("invoice_line_text", models.CharField(max_length=1000)),
            ],
        ),
    ]
