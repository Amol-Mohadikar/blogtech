# Generated by Django 3.2 on 2021-05-10 14:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20210510_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2021, 5, 10, 14, 31, 7, 2613, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='mainblogpost',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2021, 5, 10, 14, 31, 7, 2613, tzinfo=utc)),
        ),
    ]