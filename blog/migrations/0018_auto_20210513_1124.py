# Generated by Django 3.2 on 2021-05-13 05:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_auto_20210513_1118'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='thumbnail2',
            field=models.ImageField(default='', upload_to='blog/images'),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='thumbnail3',
            field=models.ImageField(default='', upload_to='blog/images'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='about',
            field=models.CharField(default='Hey Readers! Welcome to Blogtech. for more such Awesome blogs click on next blog. If you love the blog Please like , Comment and Share.', max_length=1000),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2021, 5, 13, 5, 54, 36, 319738, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='mainblogpost',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2021, 5, 13, 5, 54, 36, 320738, tzinfo=utc)),
        ),
    ]