# Generated by Django 2.0.7 on 2018-07-10 12:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Releases',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enabled', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2018, 7, 10, 21, 58, 45, 331705))),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2018, 7, 10, 21, 58, 45, 331735))),
            ],
            options={
                'db_table': 'releases',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tracks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2018, 7, 10, 21, 58, 45, 330547))),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2018, 7, 10, 21, 58, 45, 330614))),
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
