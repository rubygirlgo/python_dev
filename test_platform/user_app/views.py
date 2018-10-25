from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    return render(request,"index.html")

def login_action(request):
    if request.method=='POST':
        username=request.POST.get('username','')
        password=request.POST.get('password','')
        if password=='' or username=='':
            return render(request,"index.html",{'error':'用户或密码为空'})
        else:
            user=auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user) #跟登录功能没有关系，用来记录用户的登录状态
                response= HttpResponseRedirect("/manage/project_manage/")
                #response.set_cookie('user',username,3600)
                request.session['user']=username
                return response
            else:
                return render(request,"index.html",{'error':'username or password is wrong'})


def logout(request):
    auth.logout(request)  # 清除用户登录状态
    response=HttpResponseRedirect('/index/')
    return response