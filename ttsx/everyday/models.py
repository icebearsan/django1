from django.db import models

# Create your models here.

class UserInfo(models.Model):
    uname = models.CharField(max_length=20)
    upwd = models.CharField(max_length=40)
    umail = models.CharField(max_length=30)
    urec = models.CharField(default='',max_length=20)
    uaddress = models.CharField(default='',max_length=30)
    ucode = models.CharField(default='',max_length=6)
    uphone = models.CharField(default='',max_length=11)


