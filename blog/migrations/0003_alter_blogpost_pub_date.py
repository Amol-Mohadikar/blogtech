# Generated by Django 3.2 on 2021-05-09 06:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210509_1012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2021, 5, 9, 6, 38, 30, 798235, tzinfo=utc)),
        ),
    ]
