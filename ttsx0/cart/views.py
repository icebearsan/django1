from django.shortcuts import render
from cart.models import CartInfo,UserInfo
from django.http import JsonResponse
import everyday.dec
# Create your views here.

def add(request):
    try:
        uid = request.session.get('uid')
        gid = request.GET.get('gid')
        count = request.GET.get('count',1)

        cart = CartInfo.objects.filter(user_id=uid,goods_id=gid)
        if len(cart) ==1:
            cart1 = cart[0]
            cart1.count +=1
            cart1.save()
        else:
            cart = CartInfo()
            cart.user_id = uid
            cart.goods_id = gid
            cart.count = count
            cart.save()
        return JsonResponse({'isadd':1})
    except:
        return JsonResponse({'isadd':0})

def count(request):
    uid = int(request.session.get('uid'))
    count1 = CartInfo.objects.filter(user_id=uid).count()
    return JsonResponse({'count':count1})

def edit(request):
    id = int(request.GET.get('id'))
    count = int(request.GET.get('count'))
    cart = CartInfo.objects.get(pk=id)
    cart.count = count
    cart.save()
    return JsonResponse({'ok':1})

def delete(request):
    id = int(request.GET.get('id'))
    cart = CartInfo.objects.get(pk=id)
    cart.delete()
    return JsonResponse({'result':1})

@everyday.dec.dec
def cart(request):
    uid = int(request.session.get('uid'))
    cart_list = CartInfo.objects.filter(user_id=uid)
    return render(request,'everyday/cart.html',{'title':'购物车','cart_list':cart_list})

def order(request):
    user = UserInfo.objects.get(pk=request.session.get('uid'))
    cart_list = CartInfo.objects.filter(id__in=request.POST.getlist('cart_id'))
    context = {'title':'提交订单','user':user,'cart_list':cart_list}
    return render(request,'everyday/order.html',context)

