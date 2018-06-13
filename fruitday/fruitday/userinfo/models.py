from django.db import models

# Create your models here.

class UserInfo(models.Model):
    email = models.CharField('邮箱',max_length = 40,null=False)
    uname = models.CharField('用户名',max_length = 40,null=False)
    upassword = models.CharField('密码',max_length = 40,null=False)
    isactive = models.BooleanField('是否激活',default=True)
    phone = models.CharField('电话',max_length=40, null=False)
    isdelete = models.BooleanField('是否删除',default=False)
    
