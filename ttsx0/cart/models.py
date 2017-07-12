from django.db import models
from goods.models import GoodsInfo
from everyday.models import UserInfo
# Create your models here.

class CartInfo(models.Model):
    goods = models.ForeignKey(GoodsInfo)
    user = models.ForeignKey(UserInfo)
    count = models.IntegerField()
