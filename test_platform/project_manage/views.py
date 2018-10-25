from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from project_manage.models import project_list
#from
# Create your views here.
@login_required #判断用户是否登录
def project_manage(request):
    #username=request.COOKIES.get('user','')
    username=request.session.get("user",'')
    projectlist=project_list.objects.all()
    return render(request,"project_manage.html",{"username":username,"projects":projectlist}
    	)


@login_required
def project_add(request):
	username=request.session.get("user",'')
	return render(request,"project_manage.html",{"type":"add"})

