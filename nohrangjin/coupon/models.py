from django.db import models

# Create your models here.

class User(models.Model):
    hp = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Store(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    tel = models.CharField(max_length=200)
    img = models.TextField(default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Coupon(models.Model):
    name = models.CharField(max_length=200)
    detail = models.CharField(max_length=200)
    count = models.IntegerField(default=0)
    due = models.DateTimeField(default="")
    img = models.TextField(default="")
    store = models.ForeignKey(Store, on_delete=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class UserCoupon(models.Model):
    user = models.ForeignKey(User, on_delete=True, null=True)
    coupon = models.ForeignKey(Coupon, on_delete=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)