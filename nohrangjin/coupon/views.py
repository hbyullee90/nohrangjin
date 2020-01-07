from django.shortcuts import render
from coupon.models import Coupon, User, UserCoupon
from django.shortcuts import render, redirect
import requests

# Create your views here.
def coupon(request):
    context = {
        'coupons' : Coupon.objects.all()
    }
    return render(request, 'coupon/main.html', context)

# posts > views.py

def create(request):
    if request.method == "POST":
        hp = request.POST.get('hp')
        
        coupon_id = request.POST.get('coupon_idx')
        if User.objects.filter(hp=hp).exists()==False:
            User.objects.create(hp=hp)
        
        user = User.objects.get(hp=hp)
        coupon = Coupon.objects.get(pk=coupon_id)
     

        if UserCoupon.objects.filter(user=user, coupon=coupon).exists():
            context = {
                'result_msg' : '이미 발급받은 쿠폰입니다. :) 일주일 후에 재발급 받아주세요.'
            }
            return render(request, 'coupon/result.html', context)
        if coupon.count<1:
            context = {
                'result_msg' : '쿠폰이 전부 소진되었습니다. ㅠ.ㅠ 다른 쿠폰을 이용해주세요.'
            }
            return render(request, 'coupon/result.html', context)
        coupon.count = coupon.count -1
        coupon.save()
        UserCoupon.objects.create(user=user, coupon=coupon)
        text = "[노량진 쿠폰모아]\n가게명 : " + coupon.store.name +"\n\n" + coupon.name +"\n"+coupon.detail + "\n-"+coupon.due.strftime('%Y-%m-%d')+"까지 사용가능\n\n 매장 위치 - 노량진역 1번 출구 옆 할리스 건물 1층"
        sms_msg(hp,text)
        context = {
            'result_msg' : '쿠폰발급이 완료 되었습니다. 문자 내역을 확인하세요 :)'
        }
        return render(request, 'coupon/result.html', context)

    

def sms_msg(phone_number, text):
    userphone = phone_number

    data = {
        "remote_id": "hbyullee",
        "remote_pass": "junior",
        "remote_num": 1,
        "remote_phone": userphone,
        "remote_callback": "01082611082",
        "remote_msg": text,
    }

    # headers = {"Content-type": "Application/json"}
    r = requests.post("https://www.munja123.com/Remote/RemoteMms.html", data)
    return r.text