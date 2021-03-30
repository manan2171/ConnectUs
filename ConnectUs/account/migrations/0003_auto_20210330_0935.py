# Generated by Django 3.1.7 on 2021-03-30 04:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_friend'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friend',
            name='user1',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='user1', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='friend',
            name='user2',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='user2', to=settings.AUTH_USER_MODEL),
        ),
    ]