# Generated by Django 2.2 on 2022-11-25 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('battle_name', models.CharField(max_length=100)),
                ('monster_build', models.CharField(max_length=100)),
                ('skill_1', models.ImageField(upload_to='')),
                ('equip_1', models.CharField(max_length=200)),
                ('skill_2', models.ImageField(upload_to='')),
                ('equip_2', models.CharField(max_length=200)),
                ('skill_3', models.ImageField(upload_to='')),
                ('equip_3', models.CharField(max_length=200)),
                ('strategy', models.TextField(max_length=3000)),
            ],
        ),
    ]
