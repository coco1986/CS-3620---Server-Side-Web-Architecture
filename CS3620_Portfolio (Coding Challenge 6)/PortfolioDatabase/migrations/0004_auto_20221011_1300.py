# Generated by Django 2.2 on 2022-10-11 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PortfolioDatabase', '0003_portfolio_portfolio_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_message', models.CharField(default='https://operations.chicagopolice.org/FIMSPublic/Content/images/default-contact-image.png', max_length=500)),
            ],
        ),
        migrations.AlterField(
            model_name='hobbies',
            name='hobby_desc',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='portfolio_desc',
            field=models.CharField(max_length=500),
        ),
    ]