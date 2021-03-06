# Generated by Django 3.2.4 on 2021-09-07 02:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_edu', '0003_auto_20210904_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='time_of_comment',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 7, 8, 22, 11, 433363)),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 7, 8, 22, 11, 422265)),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_name',
            field=models.CharField(default=None, max_length=100, verbose_name='Course Name'),
        ),
        migrations.AlterField(
            model_name='notes',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 7, 8, 22, 11, 422265)),
        ),
    ]
