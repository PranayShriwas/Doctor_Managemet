# Generated by Django 4.1.5 on 2023-06-08 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Doctor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Name", models.CharField(max_length=50)),
                ("Degree", models.CharField(max_length=50)),
                ("Contact", models.CharField(max_length=100)),
                ("Email", models.EmailField(max_length=254)),
                ("Password", models.CharField(max_length=50)),
                ("Image", models.ImageField(upload_to="docimage/")),
                (
                    "Category",
                    models.CharField(
                        choices=[
                            ("lungsSpecialist", "lungsSpecialist"),
                            ("eyespecialist", "eyespecialist"),
                            ("heartspecialist", "heartspecialist"),
                            ("legspecialist", "legspecialist"),
                        ],
                        default="eyespecialist",
                        max_length=100,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Name", models.CharField(max_length=50)),
                ("Contact", models.CharField(max_length=50)),
                ("Email", models.EmailField(max_length=254)),
                ("Password", models.CharField(max_length=50)),
            ],
        ),
    ]