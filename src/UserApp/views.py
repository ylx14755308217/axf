import uuid

from PIL import Image, ImageFont
from PIL.ImageDraw import ImageDraw

from django.contrib.auth.hashers import make_password, check_password
from django.core.cache import cache
from django.core.mail import send_mail
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.template import loader
from django.urls import reverse
from django.utils.six import BytesIO

from UserApp.models import AxfUser
from UserApp.view_helper import sendEmail
from axf import settings


def register(request):
    if request.method == 'GET':
        return render(request,'axf/user/register/register.html')
    elif request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        email = request.POST.get('email')
        icon = request.FILES.get('icon')

        password = make_password(password)

        user = AxfUser()
        user.name = name
        user.password = password
        user.email = email
        user.icon = icon

        token = uuid.uuid4()
        user.token = token

        user.save()

        cache.set(token,user.id,timeout=60)
        # 发送邮件
        sendEmail(name,email,token)

        return redirect(reverse('axfuser:login'))

def login(request):
    if request.method == 'GET':
        return render(request,'axf/user/login/login.html')
    elif request.method == 'POST':
# 先判断验证码还是先判断名字和密码
# 先验证验证码 因为要较少数据库访问次数
# 页面中你输入的验证码
        imgcode = request.POST.get('imgCode')
        #图片中的验证码数字
        verify_code = request.session.get('verify_code')

        if imgcode.lower() == verify_code.lower():

            name = request.POST.get('name')
            users = AxfUser.objects.filter(name=name)

            if users.exists():
                user = users.first()

                password = request.POST.get('password')

                if check_password(password,user.password):
                    if user.active:
                        #session 不能直接绑定一个对象 可以绑定属性
                        request.session['user_id']=user.id

                        return register(reverse('axfmine:mine'))
                    else:
                        context = {
                            'msg':'账户未激活'
                        }
                        return render(request, 'axf/user/login/login.html', context=context)

                else:
                    context = {
                        'msg':'密码错误'
                    }
                    return render(request,'axf/user/login/login.html',context=context)

            else:
                context = {
                    'msg':'用户名错误'
                }
                return render(request,'axf/user/login/login.html',context=context)
        else:
            context = {
                'msg':'验证码错误'
            }
            return render(request,'axf/user/login/login.html',context=context)


def checkName(request):
    data = {
        'status': 200,
        'msg': '用户名字可以使用'
    }

    name = request.GET.get('name')
    users = AxfUser.objects.filter(name=name)
    if users.exists():
        data['msg']='用户名字已经存在'
        data['status']='201'
        return JsonResponse(data=data)
    else:
        return JsonResponse(data=data)


def account(request):
    # 将当前注册的用户的激活状态修改为True
    token = request.GET.get('token')

    user_id = cache.get(token)

    if user_id:
        user = AxfUser.objects.get(pk=user_id)
        user.active =True
        user.save()
        cache.delete(token)
        return HttpResponse('激活成功')
    else:
        return HttpResponse('邮件已过期')



def get_code(request):

    # 初始化画布，初始化画笔

    mode = "RGB"

    size = (200, 100)

    red = get_color()

    green = get_color()

    blue = get_color()

    color_bg = (red, green, blue)

    image = Image.new(mode=mode, size=size, color=color_bg)

    imagedraw = ImageDraw(image, mode=mode)
# 验证码的字体
    imagefont = ImageFont.truetype(settings.FONT_PATH, 100)

    verify_code = generate_code()

    request.session['verify_code'] = verify_code

    for i in range(4):
        fill = (get_color(), get_color(), get_color())
        imagedraw.text(xy=(50*i, 0), text=verify_code[i], font=imagefont, fill=fill)

    for i in range(1000):
        fill = (get_color(), get_color(), get_color())
        xy = (random.randrange(201), random.randrange(100))
        imagedraw.point(xy=xy, fill=fill)

    fp = BytesIO()

    image.save(fp, "png")

    return HttpResponse(fp.getvalue(), content_type="image/png")









import random


def get_color():
    return random.randrange(256)


def generate_code():
    source = "qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM"

    code = ""

    for i in range(4):
        code += random.choice(source)

    return code


def logout(request):
    request.session.flush()
    return redirect(reverse('axfmine:mine'))