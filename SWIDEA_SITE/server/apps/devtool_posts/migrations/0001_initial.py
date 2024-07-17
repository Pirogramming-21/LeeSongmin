# Generated by Django 5.0.7 on 2024-07-17 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DevtoolPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('kind', models.IntegerField(max_length=30)),
                ('content', models.TextField(max_length=100, verbose_name='개발툴 설명')),
            ],
        ),
    ]