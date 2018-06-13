from django.db import models

# Create your models here.


class GoodsType(models.Model):
    title = models.CharField('名称', max_length=30)
    desc = models.CharField('描述',max_length=200)
    picture = models.ImageField(upload_to = 'static/image')
    isdelete = models.BooleanField(default=False)

class Goods(models.Model):
    title = models.CharField('名称', max_length=50)
    price = models.DecimalField('价格', max_digits=8,decimal_places=2)
    desc = models.CharField('描述',max_length=200)
    picture = models.ImageField(upload_to='static/image')
    isdelete = models.BooleanField(default=False)
    type = models.ForeignKey(GoodsType)