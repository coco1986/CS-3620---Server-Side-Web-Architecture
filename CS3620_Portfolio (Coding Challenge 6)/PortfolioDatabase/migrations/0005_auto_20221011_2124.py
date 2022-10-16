# Generated by Django 2.2 on 2022-10-12 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PortfolioDatabase', '0004_auto_20221011_1300'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='contact_message',
        ),
        migrations.AddField(
            model_name='contact',
            name='c_email',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='contact',
            name='c_message',
            field=models.CharField(default='Personal Message goes here.', max_length=500),
        ),
        migrations.AddField(
            model_name='contact',
            name='c_name',
            field=models.CharField(default='', max_length=200),
        ),
    ]
