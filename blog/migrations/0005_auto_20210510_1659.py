# Generated by Django 3.2 on 2021-05-10 11:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20210510_1637'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Mainblogpost',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='made_by',
            field=models.CharField(default='Blogtech Admin', max_length=25),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='maintitle1',
            field=models.CharField(default='no title', max_length=50),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='maintitle2',
            field=models.CharField(default='no title', max_length=50),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='maintitle3',
            field=models.CharField(default='no title', max_length=50),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='paragraph1',
            field=models.CharField(default='', max_length=5000),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='paragraph2',
            field=models.CharField(default='', max_length=5000),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='paragraph3',
            field=models.CharField(default='', max_length=5000),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2021, 5, 10, 11, 29, 46, 203228, tzinfo=utc)),
        ),
    ]