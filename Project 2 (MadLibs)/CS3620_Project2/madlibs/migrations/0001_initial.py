# Generated by Django 2.2 on 2022-10-18 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Madlibs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('noun', models.CharField(default='', max_length=20)),
                ('adjective', models.CharField(default='', max_length=20)),
                ('city', models.CharField(default='', max_length=20)),
                ('noun2', models.CharField(default='', max_length=20)),
                ('pronoun', models.CharField(default='', max_length=20)),
                ('verb', models.CharField(default='', max_length=20)),
                ('noun3', models.CharField(default='', max_length=20)),
            ],
        ),
    ]
