# Generated by Django 2.2 on 2022-10-30 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(default='images/none/noimg.jpg', upload_to='images'),
        ),
    ]
