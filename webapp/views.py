from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpRequest
from django.http import HttpRequest
from django.http import HttpResponse
from django.template import RequestContext
from django.contrib import auth
from django.contrib.auth.models import User
from .models import GOOD
from .models import enterprise_ORDER
from .models import useradd
import datetime


# Create your views here.

def home(request):
    return render(request, 'homepage.html')


def log(request, url):
    if request.POST:
        userid = request.POST['userID']
        passwd = request.POST['passwd']
        user = auth.authenticate(username=userid, password=passwd)
        if user is not None and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(url)
        else:
            return HttpResponseRedirect("/")
            # 加入登录失败警告框
            # message="登录失败请重新登陆"
            # return render(request,'homepage.html',)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')


def sign_up(request):
    return render(request, 'sign up.html')


def sign(request):
    if request.POST:
        userid = request.POST['userID']
        passwd = request.POST['passwd']
        passwd_re = request.POST['passwd_re']
        name = request.POST['name']
        try:
            if passwd == passwd_re:
                user = User.objects.create_user(name, userid, passwd)
                user.save()
            else:
                message = u'两次密码不同'
                return render(request, 'sign up.html', {'message': message})
        except:
            message = u'注册失败,请重新注册'
            return render(request, 'sign up.html', {'message': message})
    return HttpResponseRedirect('/')

def chpwd(request):
    return render(request,"change_password.html")

def chpwd_r(request):
    if request.POST:
        oldpwd=request.POST['oldpwd']
        newpwd=request.POST['newpwd']
        newpwd_re=request.POST['newpwd_re']
        user = auth.authenticate(username=request.user.get_username(), password=oldpwd)
        try:
            if user is None:
                message = u'原密码不正确'
                return render(request, 'change_password.html', {'message': message})
            elif newpwd !=newpwd_re:
                message = u'两个密码不同'
                return render(request, 'change_password.html', {'message': message})
            else:
                user.set_password(newpwd)
                user.save()
                return HttpResponse('修改成功')
        except:
            return HttpResponse('修改失败')

def about(request):
    return render(request,"sale.html")

def manageorder(request):
    if request.user.is_superuser:
        data = enterprise_ORDER.objects.all()
        return render(request, 'managerorder.html', {'data': data})
    else:
        return HttpResponse('无法访问')


def manageorder_yes(request):
    data = enterprise_ORDER.objects.filter(Status=100)
    return render(request, 'managerorder.html', {'data': data})


def manageorder_no(request):
    data = enterprise_ORDER.objects.filter(Status=200)
    return render(request, 'managerorder.html', {'data': data})


def manageorder_delete(request):
    if request.POST:
        check_box_list = request.POST.getlist('order')
        for i in check_box_list:
            enterprise_ORDER.objects.filter(OrderID=int(i)).delete()
    return HttpResponseRedirect('/manageorder1')


def order_change(request):
    if request.POST:
        check_box_list = request.POST.getlist('order')
        for i in check_box_list:
            enterprise_ORDER.objects.filter(OrderID=int(i)).update(Status=300)
    return HttpResponseRedirect('/manageorder1')


def manageuser(request):
    if request.user.is_superuser:
        data = User.objects.all()
        return render(request, 'manageuser.html', {'data': data})
    else:
        return HttpResponse('无法访问')


def managegood(request):
    data = GOOD.objects.all()
    return render(request, "managegood.html", {'data': data})


def sale(request):
    data = GOOD.objects.all()
    return render(request, 'buy.html',{'data':data})
    # 加载商品数据库


def buyview(request, name):
    data = GOOD.objects.filter(GoodID=name)
    return render(request, 'good_detail.html', {'data': data, 'name': name})


def sort_by_high(request):
    pass


def sort_by_low(request):
    pass


def shopping(request, name):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/')
    elif request.user.is_authenticated():
        data_G = GOOD.objects.filter(GoodID=name)
        return render(request, 'shopping.html', {'data': data_G, 'name': name})


def buy(request, name):
    if request.POST:
        try:
            data = GOOD.objects.get(GoodID=name)
            i = len(enterprise_ORDER.objects.filter(DATE=datetime.date.today()))
            order = enterprise_ORDER()
            order.UserID = User.objects.get(username=request.user.get_username())
            order.DATE = datetime.date.today()
            order.Price1 = data.GoodPrice
            order.GoodID = data
            order.ADDRESS = request.POST['address']
            order.OrderID = int(str(datetime.date.today()).replace('-', '')) * 1000 + i
            print(order.OrderID)
            order.Telephone = request.POST['telephone']
            order.Status = 100
            order.save()
            return HttpResponse('购买成功')
        except:
            return HttpResponse('购买失败')


def pay(request):
    pass



