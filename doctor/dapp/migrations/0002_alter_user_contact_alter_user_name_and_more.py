# Generated by Django 4.1.5 on 2023-06-08 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user", name="Contact", field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="user", name="Name", field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="user", name="Password", field=models.CharField(max_length=100),
        ),
    ]