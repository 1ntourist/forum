# Generated by Django 2.2.8 on 2020-01-11 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0003_auto_20200111_0114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ads',
            name='file',
            field=models.FileField(default='images/default.png', upload_to='images/'),
        ),
    ]
