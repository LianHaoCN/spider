# _*_ coding:utf-8 _*_  
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
#from django.shortcuts import render
from django.template import RequestContext

from spider.constant import USAGE_CHOICES

@login_required(login_url='/login')
def index(request):
    return render_to_response('index.html')
    
def login(request):
    if request.session.get('username') is not None:
        return HttpResponseRedirect('/',{"user":request.user})
    else:
        username = request.POST.get('username')
        password = request.POST.get('password') 
        user = auth.authenticate(username=username,password=password)
        if user and user.is_active:
            auth.login(request,user)
            request.session['username'] = username
            return HttpResponseRedirect('/user/center/',{"user":request.user})
        else:
            if request.method == "POST":
                return render_to_response('login.html', {'usage':USAGE_CHOICES, "login_error_info":"用户名不错存在，或者密码错误！"},
                                                        context_instance=RequestContext(request))  
            else:
                return render_to_response('login.html', {'usage':USAGE_CHOICES}, context_instance=RequestContext(request))
    
def test(request):
    """展示登录界面"""
    return render(request, 'test.html', {'usage': USAGE_CHOICES})