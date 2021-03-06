# Generated by Django 2.0.7 on 2018-07-10 13:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subscribes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enabled', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2018, 7, 10, 22, 4, 20, 682722))),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2018, 7, 10, 22, 4, 20, 682759))),
            ],
            options={
                'db_table': 'subscribes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tracks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2018, 7, 10, 22, 4, 20, 681834))),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2018, 7, 10, 22, 4, 20, 681867))),
            ],
            options={
                'db_table': 'tracks',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
    ]
