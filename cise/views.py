from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from cise.models import User
from django.urls import reverse
# Create your views here.


def index(request):
    return render(request, 'cise/index.html')


def login(request):
    # return render(request, 'cise/login.html')
    if request.method == 'GET':
        return render(request, 'cise/login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username=username).first()
        if user:
            if user.password == password:
                return HttpResponse('登录成功')
            else:
                return HttpResponse('密码错误')
        else:
            return HttpResponse('用户名错误')


def register(request):
    # return render(request, 'cise/register.html')
    if request.method == 'GET':
        return render(request, 'cise/register.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        q = User(username=username, password=password)
        q.save()
        return HttpResponseRedirect(reverse('login'))
