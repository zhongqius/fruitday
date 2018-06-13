from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password,make_password
from django.core.exceptions import ObjectDoesNotExist
from .models import *
import logging
# Create your views here.

def signin(request):
    return render(request,'login.html')


def login_(request):
    if request.method == 'POST':
        user = UserInfo()
        user.uname = request.POST.get('username')
        user.upassword = request.POST.get('pwd')
        try:
            find_user = UserInfo.objeces.filter(uname=user.uname)
            if len(find_user) <= 0:
                return render(request,'login.html',{'massage':'用户名未注册'})
            if not check_password(user.upassword,find_user[0].upassword):
                return render(request,'login.html',{'massage':'账号密码错误'})
        except ObjectDoesNotExist as e:
            logging.warning(e)
        if not find_user[0].isdelete:
            return render(request,'login.html',{'massage':'账号不存在'})
        if find_user[0].isactive:
            return render(request,'login.html',{'massage':'账号已激活'})
        request.session['user_id'] = find_user[0].id
        request.session['user_name'] = find_user[0].uname
        return render(request, 'index.html')

