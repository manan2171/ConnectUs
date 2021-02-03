from django.db import models
from django.utils import timezone
# Create your models here.


class user(models.Model):
    user_name=models.CharField(max_length=20)
    user_id=models.IntegerField(primary_key=True,default=0)
    user_dob=models.DateTimeField(default=timezone.now())