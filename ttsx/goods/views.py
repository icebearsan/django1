from django.shortcuts import render
from goods.models import *
# Create your views here.
def index(request):
    type_list = TypeInfo.objects.all()
    list1 = []
    for type1 in type_list:
        new_list = type1.goodsinfo_set.order_by('-id')[0:4]
        click_list = type1.goodsinfo_set.order_by('-gclick')[0:4]
        list1.append({'new_list':new_list,'click_list':click_list})
        return render(request,'everyday/index.html',{'title':'shouye','list1':list1,'cart':'1'})

def goods_list(request,tid):
    t1 = TypeInfo.objects.get(pk=int(tid))
    new_list = t1.goodsinfo_set.order_by('-id')[0:2]
    context = {'title':'商品列表','cart':'1','t1':t1,'new_list':new_list}
    return render(request,'everyday/list.html',context)