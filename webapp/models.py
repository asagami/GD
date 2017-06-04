from django.db import models
from django.contrib.auth.models import User
from django.contrib import auth
# Create your models here.

class GOOD(models.Model):
    GoodID = models.IntegerField(null=False, primary_key=True)
    GoodName = models.CharField(null=False, max_length=20, default='  ')
    GoodPrice = models.FloatField(null=False)
    GoodPrice1=models.FloatField(null=False)
    GoodPrice2=models.FloatField(null=False)
    GoodImage=models.ImageField(null=False)
    GoodStock=models.IntegerField(null=False,default=0)
    def __str__(self):
        return self.GoodName

class enterprise_ORDER(models.Model):
    UserID = models.ForeignKey(User)
    GoodID=models.ForeignKey(GOOD)
    OrderName = models.CharField(max_length=50, null=False)
    OrderID = models.FloatField(null=False,primary_key=True,max_length=100)
    ADDRESS = models.CharField(null=False, max_length=100)
    DATE = models.DateField(auto_now_add=False, null=True)
    DES = models.TextField(null=True)
    Price1 = models.CharField(null=False,max_length=11)
    Telephone = models.FloatField(null=False,max_length=100)
    Status = models.IntegerField(null=False,default=100)
    #状态码表示意思：100 订单下达  ， 200 订单支付 ，300 订单完成
    def __str__(self):
        return self.OrderName

class useradd(models.Model):
   UserName=models.ForeignKey(User)
   UserTelephone=models.IntegerField(null=False)
   UserAddress_deafult=models.CharField(max_length=100,null=False)

class pay(models.Model):
    Username=models.ForeignKey(User)
    OrderID=models.ForeignKey(enterprise_ORDER)
    alipayID=models.CharField(null=False,max_length=100,default='0')

