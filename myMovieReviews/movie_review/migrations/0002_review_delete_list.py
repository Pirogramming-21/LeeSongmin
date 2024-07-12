# Generated by Django 5.0.7 on 2024-07-12 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_review', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('year', models.CharField(max_length=10)),
                ('genre', models.CharField(max_length=10)),
                ('score', models.CharField(max_length=10)),
                ('running_time', models.CharField(max_length=20)),
                ('content', models.TextField()),
                ('director', models.CharField(max_length=20)),
                ('actors', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='List',
        ),
    ]
