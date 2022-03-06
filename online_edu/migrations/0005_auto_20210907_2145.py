# Generated by Django 3.2.4 on 2021-09-07 16:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_edu', '0004_auto_20210907_0822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='time_of_comment',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 7, 21, 45, 38, 383651)),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 7, 21, 45, 38, 375067)),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_thumbnail',
            field=models.URLField(default=None, verbose_name='Course Thumbnail URL'),
        ),
        migrations.AlterField(
            model_name='notes',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 7, 21, 45, 38, 376069)),
        ),
    ]