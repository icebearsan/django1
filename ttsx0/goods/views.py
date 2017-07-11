from django.shortcuts import render
from goods.models import *
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    type_list = TypeInfo.objects.all()
    list1 = []
    for type1 in type_list:
        new_list = type1.goodsinfo_set.order_by('-id')[0:4]
        click_list = type1.goodsinfo_set.order_by('-gclick')[0:4]
        list1.append({'new_list':new_list,'click_list':click_list})
        return render(request,'everyday/index.html',{'title':'首页','list1':list1,'cart':'1'})

def goods_list(request,tid,pindex,orderby):
    t1 = TypeInfo.objects.get(pk=int(tid))
    orderby_str = '-id'
    desc = '1'
    if int(orderby) == 2:
        desc = request.GET.get('desc')
        if desc == '1':
            orderby_str = 'gprice'
        else:
            orderby_str = '-gprice'
    elif int(orderby) == 3:
        orderby_str = 'gclick'
    new_list = t1.goodsinfo_set.order_by('-id')[0:2]
    glist = t1.goodsinfo_set.order_by(orderby_str)
    paginator = Paginator(glist,10)
    pindex1= int(pindex)
    if pindex1<1:
        pindex1 = 1
    if pindex1>paginator.num_pages:
        pindex1 = paginator.num_pages
    page = paginator.page(pindex1)
    context = {'title':'商品列表','cart':'1','t1':t1,'new_list':new_list,'page':page,'orderby':orderby,'desc':desc}
    return render(request,'everyday/list.html',context)

def detail(request,id):
    try:
        goods = GoodsInfo.objects.get(pk=int(id))
        goods.gclick+=1
        goods.save()
        new_list = goods.gtype.goodsinfo_set.order_by('-id')[0:2]
        context = {'title':'详细商品页','cart':'1','new_list':new_list,'goods':goods}
        response = render(request, 'everyday/detail.html', context)
        ids = request.COOKIES.get('goods_ids','').split(',')
        if id in ids:
            ids.remove(id)
        ids.insert(0,id)
        if len(ids) > 5:
            ids.pop()
        response.set_cookie('goods_ids',','.join(ids),max_age=60*60*24*7)
        return response
    except:
        return render(request,'404.html')