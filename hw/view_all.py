# -*- coding: utf-8 -*-
from django.shortcuts import render,HttpResponseRedirect
from modelapp.models import Test,abc,ssr_1
from . import linux_shell,ping,tcp,ssr
from django.contrib.auth.models import auth,User
from django.contrib.auth.decorators import login_required
import requests,base64,os


last_port=1
ip='xx'

def code_haimianbaobao(s):
    a=os.system('myqr '+s+' -p C:/Users/Administrator/Desktop/project/ssr_scr/erweima.jpg -d C:/Users/Administrator/Desktop/project/ssr_scr/static/ -n 1.png -c')
    print(a)

def add_port(port):#数据库增加数据 ssr_1就代表表名，通过继承model类来完成数据库操作
    test1=ssr_1(name=str(port))
    test1.save()


def get_last_port():
    list = ssr_1.objects.all()#获取所有数据
    list_data=[]
    for var in list:
        list_data.append(var.name) 
    return list_data[-1]

@login_required(login_url='/login')#修饰需要登录权限的页面
def post(request):#post1代表工具接口 ping和tcp检测
    context={}
    _ping=ping.ping()
    _tcp=tcp.tcp()
    if  "+" in _ping:
        context['cping']=1
    else:
        context['cping']=0
    if  "+" in _tcp:
        context['ctcp']=1
    else:
        context['ctcp']=0
    context['ping']=_ping
    context['tcp']=_tcp
    context['port']=get_last_port()
    context['ping1']='ping检测：'
    context['tcp1']='tcp检测：'
    context['port1']='当前端口：'
    _t=requests.get('http://cnmf.net.cn/xx.html').text
    _t=base64.b64decode(_t).decode()
    code_haimianbaobao(_t)
    context['haimianbaobao']='/static/1.png'
    context['dy'] = _t

    context['dy1']='当前地址（订阅已自动更新：cnmf.net.cn/xx.html）：'
    return render(request,'a.html',context)

text='iptables: Saving firewall rules to /etc/sysconfig/iptables: [ OK ]\r\niptables: Setting chains to policy ACCEPT: filter [ OK ]\r\niptables: Flushing firewall rules: [ OK ]\r\niptables: Unloading modules: [ OK ]\r\niptables: Applying firewall rules: [ OK ]\r\nIPv6 support\nstopped\nStopping ShadowsocksR success\nIPv6 support\nStarting ShadowsocksR success\n'
@login_required(login_url='/login')
def post2(request):#post2更换ip返回数据由ssr制作订阅链接
    context={}
    _re=linux_shell.main()
    add_port(str(_re)[:6])
    if text == str(text):
        context['cping']=1
        context['ping1']='更换成功！'
        ssr.main()
        _t=requests.get('http://cnmf.net.cn/xx.html').text
        _t=base64.b64decode(_t).decode()
        code_haimianbaobao(_t)
        context['haimianbaobao']='/static/1.png'
        context['dy'] = _t
        context['dy1']='当前地址（订阅已自动更新：cnmf.net.cn/xx.html）：'
    else:
        context['cping']=0
        context['ping1']='更换失败！'
    context['ping']=_re
    return render(request,'a.html',context)


def post3(request):#post3完成登录操作
  if request.method == 'POST':
    name = 'admin1'
    pwd = request.POST.get('pwd')
    print(pwd)
    user = auth.authenticate(request,username=name,password=pwd)
    if user:
        auth.login(request,user)
        return HttpResponseRedirect('/')
  return HttpResponseRedirect('login.html')


@login_required(login_url='/login')
def hello(request):
    context = {}
    _t=requests.get('http://cnmf.net.cn/xx.html').text
    _t=base64.b64decode(_t).decode()
    context['dy'] = _t
    code_haimianbaobao(_t)
    context['haimianbaobao']='/static/1.png'
    context['dy1']='当前地址（订阅已自动更新：cnmf.net.cn/xx.html）：'
    return render(request, 'a.html', context)


def login(request):
    return render(request,'login.html')