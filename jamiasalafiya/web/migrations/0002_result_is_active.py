# Generated by Django 3.2.4 on 2021-06-06 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("web", "0001_initial")]

    operations = [
        migrations.AddField(
            model_name="result",
            name="is_active",
            field=models.BooleanField(default=True),
        )
    ]
