# Generated by Django 4.1.11 on 2024-02-20 12:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_title', models.CharField(max_length=200)),
                ('work_picture', models.ImageField(upload_to='')),
                ('work_year', models.IntegerField()),
                ('work_presentaion', models.TextField(max_length=2000)),
                ('work_problems', models.TextField(max_length=2000)),
                ('work_project_url', models.URLField(blank=True, null=True)),
                ('work_github_url', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='WorkTechnology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tech', models.CharField(max_length=50)),
                ('work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='work_technology', to='Work.work')),
            ],
        ),
    ]
