# Generated by Django 3.1.7 on 2021-03-13 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("app", "0001_initial")]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="file",
            field=models.FileField(blank=True, max_length=128, null=True, upload_to=""),
        ),
        migrations.AlterField(
            model_name="book",
            name="subtitle",
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
