# Generated by Django 2.2.1 on 2019-07-14 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='pics/'),
        ),
    ]