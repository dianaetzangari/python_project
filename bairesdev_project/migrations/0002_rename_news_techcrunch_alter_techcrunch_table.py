# Generated by Django 4.0.1 on 2022-01-14 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bairesdev_project', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='news',
            new_name='TechCrunch',
        ),
        migrations.AlterModelTable(
            name='techcrunch',
            table='techcrunch',
        ),
    ]
