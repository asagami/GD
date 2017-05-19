from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpRequest
from django.http import HttpResponse
from django.template import RequestContext
from django.contrib import auth
from django.contrib.auth.models import User
from .models import GOOD
# Create your views here.

def home(request):
    return  render(request,'homepage.html')

def log(request,url):
    if request.POST:
        userid = request.POST['userID']
        passwd = request.POST['passwd']
        user = auth.authenticate(username=userid, password=passwd)
        if user is not None and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(url)
        else:
            return HttpResponseRedirect("/")
            #加入登录失败警告框
            #message="登录失败请重新登陆"
            #return render(request,'homepage.html',)

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

def manage(request):
    return render(request,'manage.html')