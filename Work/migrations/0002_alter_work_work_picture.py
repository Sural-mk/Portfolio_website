# Generated by Django 4.1.11 on 2024-02-20 20:05

import Work.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Work', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='work_picture',
            field=models.ImageField(upload_to=Work.models.work_directory_path),
        ),
    ]
