# Generated by Django 3.2.4 on 2021-09-04 09:32

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('online_edu', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(default=None, max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='notes',
            name='thubmnail',
        ),
        migrations.AddField(
            model_name='notes',
            name='like',
            field=models.ManyToManyField(blank=True, related_name='users', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='notes',
            name='thumbnail',
            field=models.URLField(blank=True, default=None, verbose_name='Thumbnail'),
        ),
        migrations.AddField(
            model_name='user',
            name='lecturer',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='notes',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 4, 15, 2, 41, 400989)),
        ),
        migrations.AlterField(
            model_name='notes',
            name='video_iframe',
            field=models.TextField(blank=True, null=True, verbose_name='Video iframe'),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follower', models.ManyToManyField(blank=True, related_name='following', to=settings.AUTH_USER_MODEL)),
                ('following', models.ManyToManyField(blank=True, related_name='followers', to=settings.AUTH_USER_MODEL)),
                ('person', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='person', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(default=None, max_length=200, verbose_name='Course Name')),
                ('course_description', models.TextField(default=None, max_length=200, verbose_name='Course Description')),
                ('course_date', models.DateTimeField(default=datetime.datetime(2021, 9, 4, 15, 2, 41, 400989))),
                ('course_thumbnail', models.URLField(default=None, verbose_name='Course Thumbnail')),
                ('course_category', models.ForeignKey(blank=True, null=True, on_delete=models.SET('Miscellaneous'), to='online_edu.category', verbose_name='Course Category')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Course Creator')),
                ('subscribed_users', models.ManyToManyField(blank=True, related_name='subscribed_users', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_of_comment', models.DateTimeField(default=datetime.datetime(2021, 9, 4, 15, 2, 41, 408290))),
                ('comment', models.TextField(default=None, verbose_name='Comment')),
                ('commenter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commenter', to=settings.AUTH_USER_MODEL)),
                ('listing_commented', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='online_edu.notes')),
            ],
        ),
        migrations.AddField(
            model_name='notes',
            name='course',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='online_edu.course', verbose_name='Course'),
        ),
        migrations.AlterField(
            model_name='notes',
            name='category',
            field=models.ForeignKey(on_delete=models.SET('Miscellaneous'), to='online_edu.category', verbose_name='Category'),
        ),
    ]
