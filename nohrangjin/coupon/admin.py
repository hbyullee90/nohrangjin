from django.contrib import admin
from .models import Coupon, User, Store, UserCoupon
# Register your models here.
@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'detail',
        'count',
        'due',
        'store',
        'created_at',
        'updated_at'
    )

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'hp',
        'created_at',
        'updated_at'
    )
    
@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'location',
        'tel',
        'created_at',
        'updated_at'
    )
    
@admin.register(UserCoupon)
class UserCouponAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'coupon',
        'created_at',
        'updated_at'
    )
