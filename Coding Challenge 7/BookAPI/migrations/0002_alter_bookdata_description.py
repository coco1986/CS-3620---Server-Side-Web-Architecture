# Generated by Django 4.1.2 on 2022-10-25 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookAPI', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookdata',
            name='description',
            field=models.CharField(max_length=500),
        ),
    ]
