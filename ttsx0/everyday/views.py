# coding=utf-8
from django.shortcuts import render,redirect
from hashlib import  sha1
from everyday.models import UserInfo
from goods.models import GoodsInfo
from django.http import JsonResponse
import datetime
import everyday.dec
# Create your views here.

def register(request):
    return render(request,'everyday/register.html',{'title':'注册','top':'0'})

def register_handle(request):
    p = request.POST
    uname = p.get('user_name')
    upwd = p.get('pwd').encode('utf-8')
    uemail = p.get('email')

    s1 = sha1()
    s1.update(upwd)
    upwd_sha1 = s1.hexdigest()

    user = UserInfo()
    user.uname = uname
    user.upwd = upwd_sha1
    user.umail = uemail
    user.save()

    return redirect('/user/login/')

def register_vaild(request):
    p = request.GET.get('uname')
    data = UserInfo.objects.filter(uname=p).count()
    return JsonResponse({'vaild':data})

def login(request):
    uname = request.COOKIES.get('uname','')
    return render(request,'everyday/login.html',{'title':'登陆','uname':uname,'top':'0'})

def login_handle(request):
    p = request.POST
    uname = p.get('username')
    upwd = p.get('pwd').encode('utf-8')
    urem = p.get('rem',0)

    s1 = sha1()
    s1.update(upwd)
    upwd_sha1 = s1.hexdigest()
    user = UserInfo.objects.filter(uname=uname)

    if len(user)==0:

        return render(request,'everyday/login.html',{'context_n':'用户名错误','title': '登录','uname':uname,'upwd':upwd,'top':'0'})
    else:
        if user[0].upwd == upwd_sha1:
            response = redirect(request.session.get('url_path', '/user/'))
            request.session['uid'] = user[0].id
            request.session['uname'] = user[0].uname
            if urem == '1':
                response.set_cookie('uname',uname,expires=datetime.datetime.now() + datetime.timedelta(days = 14))
            else:
                response.set_cookie('uname','',max_age=-1)
            return response
        else:
            return render(request,'everyday/login.html',{'context_p':'密码错误','title': '登录','uname':uname,'upwd':upwd,'top':'0'})


def log_out(request):
    request.session.flush()
    return redirect('/user/login/')

@everyday.dec.dec
def center(request):
    user = UserInfo.objects.get(pk=request.session['uid'])
    ids = request.COOKIES.get('goods_ids','').split(',')
    glist = []
    for id in ids:
        if id!='':
            glist.append(GoodsInfo.objects.get(id=id))
    return render(request,'everyday/center.html',{'user':user,'glist':glist})

@everyday.dec.dec
def order(request):
    return render(request,'everyday/order.html')

@everyday.dec.dec
def site(request):
    user = UserInfo.objects.get(pk=request.session['uid'])
    if request.method == 'POST':
        p = request.POST
        uname = p.get('uname')
        urec  = p.get('urec')
        uaddress = p.get('uaddress')
        ucode = p.get('ucode')
        uphone = p.get('uphone')

        user.urec = urec
        user.uaddress = uaddress
        user.ucode = ucode
        user.uphone = uphone
        user.save()
    return render(request,'everyday/site.html',{'user':user})


