# Generated by Django 4.2.2 on 2023-07-10 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('img', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='img',
            name='image',
            field=models.ImageField(max_length=255, null=True, upload_to='img/'),
        ),
    ]