# Generated by Django 2.2.8 on 2020-01-11 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_customuser_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='img',
            field=models.ImageField(default='images/user.png', upload_to='images/'),
        ),
    ]