from django.db import models
from userinfo.models import UserInfo
from memberapp.models import Goods
# Create your models here.

ORDERSTATUS = (
        (1,'未支付',),
        (2,'支付中',),
        (3,'已支付',),
        (4,'订单取消',),
    )

class CartInfo(models.Model):
    user = models.ForeignKey(UserInfo)
    good = models.ForeignKey(Goods)
    ccount = models.IntegerField('数量')


class Order(models.Model):
    user = models.ForeignKey(UserInfo)
    orderNo = models.CharField('订单号',max_length=50)
    ads = models.CharField('收货人', max_length =200)
    acot = models.IntegerField('总数')
    cals = models.TextField('商品详细信息',null = True)
    orderStatus = models.IntegerField('订单状态',choices=ORDERSTATUS,default=1)
