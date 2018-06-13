from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password, make_password
from django.core.exceptions import ObjectDoesNotExist
from .models import *
import logging
# Create your views here.


def signin(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')


def login_(request):
    if request.method == 'POST':
        user = UserInfo()
        user.uname = request.POST.get('username')
        user.upassword = request.POST.get('pwd')
        try:
            find_user = UserInfo.objeces.filter(uname=user.uname)
            if len(find_user) <= 0:
                return render(request, 'login.html', {'massage': '用户名未注册'})
            if not check_password(user.upassword, find_user[0].upassword):
                return render(request, 'login.html', {'massage': '账号密码错误'})
        except ObjectDoesNotExist as e:
            logging.warning(e)
        if not find_user[0].isdelete:
            return render(request, 'login.html', {'massage': '账号不存在'})
        if find_user[0].isactive:
            return render(request, 'login.html', {'massage': '账号已激活'})
        request.session['user_id'] = find_user[0].id
        request.session['user_name'] = find_user[0].uname
        return render(request, 'index.html')


def register_(request):
    if request.method == 'POST':
        new_user = UserInfo()
        new_user.uname = request.POST.get('username')
    try:
        olduser = UserInfo.objeces.filter(uname=new_user.uname)
        if len(olduser) > 0:
            return render(request, 'register.html', {'massage': '账号已存在'})
    except ObjectDoesNotExist as e:
        logging.warning(e)
    if request.POST.get('upwd') != request.POST.get('cpwd'):
        return render(request, 'register.html', {'massage': '两次密码不一致,请重新输入'})
    new_user.upassword = make_password(
        request.POST.get('upwd'), 'python', 'pbkdf2_sha1')
    new_user.email = request.POST.get('email')
    new_user.phone = request.POST.get('phone')
    try:
        new_user.save()
    except ObjectDoesNotExist as e:
        logging.warning(e)
    return render(request, 'login.html')

