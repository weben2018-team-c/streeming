from django.db import models
from datetime import datetime
import pytz


class Tracks(models.Model):
    title = models.TextField()
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(default=datetime.now(pytz.timezone('Asia/Tokyo')).replace(tzinfo=None))
    updated_at = models.DateTimeField(default=datetime.now(pytz.timezone('Asia/Tokyo')).replace(tzinfo=None))

    class Meta:
        managed = False
        db_table = 'tracks'


class Users(models.Model):
    username = models.TextField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class Subscribes(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='user')
    artist = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='artist')
    enabled = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=datetime.now(pytz.timezone('Asia/Tokyo')).replace(tzinfo=None))
    updated_at = models.DateTimeField(default=datetime.now(pytz.timezone('Asia/Tokyo')).replace(tzinfo=None))

    class Meta:
        managed = False
        db_table = 'subscribes'
