# Generated by Django 4.0.1 on 2022-01-14 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bairesdev_project', '0004_news_page'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='date',
            field=models.DateField(),
        ),
    ]