# Generated by Django 3.1.6 on 2021-02-03 10:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20210203_1541'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_dob',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 3, 10, 14, 38, 137656, tzinfo=utc)),
        ),
    ]