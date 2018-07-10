# Generated by Django 2.0.7 on 2018-07-10 14:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('play', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Releases',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enabled', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2018, 7, 10, 23, 11, 31, 579105))),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2018, 7, 10, 23, 11, 31, 579135))),
            ],
            options={
                'db_table': 'releases',
                'managed': False,
            },
        ),
    ]