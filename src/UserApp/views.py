import uuid

from django.urls import reverse
from django.utils.six import BytesIO
# 市面会有很多的验证码  那么验证码的类 大部分都是依赖于pillow
# image和imageFont的包千万注意
from PIL import Image
from PIL import ImageFont
from PIL.ImageDraw import ImageDraw

from django.contrib.auth.hashers import make_password, check_password
from django.core.cache import cache
from django.core.mail import send_mail
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.template import loader


from UserApp.models import AxfUser
from UserApp.view_helper import sendEmail
from axf import settings


def register(request):
    if request.method == 'GET':
        return render(request,'axf/user/register/register.html')
    elif request.method == 'POST':
        # 注册
        # get方法中 应该写的页面中的name的属性值
        name = request.POST.get('name')
        password = request.POST.get('password')
        email = request.POST.get('email')
        icon = request.FILES.get('icon')

        #  check_password()
        password = make_password(password)

        user = AxfUser()
        user.name = name
        user.password = password
        user.email = email
        user.icon = icon

        token = uuid.uuid4()
        user.token = token

        user.save()

        # token   id
        cache.set(token,user.id,timeout=60)
        # 发送邮件    celery异步队列 来发送邮件
        sendEmail(name,email,token)

        return redirect(reverse('axfuser:login'))


def login(request):
    if request.method == 'GET':
        return render(request,'axf/user/login/login.html')
    elif request.method == 'POST':
        # 先判断验证码还是先判断用户名字和密码
        # 先验证验证码 因为要较少数据库的访问次数
        # 页面中你输入的验证码
        imgcode = request.POST.get('imgCode')
        # 图片中的验证码的数字
        verify_code = request.session.get('verify_code')

        if imgcode.lower() == verify_code.lower():
            name = request.POST.get('name')

            users = AxfUser.objects.filter(name=name)

            if users.exists():

                user = users.first()
                # 注册时候的密码 是进行前端加密之后 才传入到的视图函数的
                # 然后再视图函数中又进行了后端加密
                # eg： 110 ===》前端  fjdksjflkdsjfdfd ==》make_password

                password = request.POST.get('password')

                if check_password(password,user.password):
                    if user.active:

                        # session不能直接绑定一个对象 可以绑定一个对象的属性
                        request.session['user_id']=user.id

                        return redirect(reverse('axfmine:mine'))
                    else:
                        context = {
                            'msg':'账户未激活'
                        }
                        return render(request,'axf/user/login/login.html',context=context)
                else:
                    context = {
                        'msg':'密码错误'
                    }
                    return render(request,'axf/user/login/login.html',context=context)
            else:
                context = {
                    'msg':'用户名字错误'
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

    # 获取单个数据   get first last count exists
    if users.exists():
        data['msg']='用户名字已经存在'
        data['status']=201
        return JsonResponse(data=data)
    else:
        return JsonResponse(data=data)


def testEmail(request):

    # subject, message, from_email, recipient_list,
    # 主题
    subject='激活'
    # 邮件的内容
    message = '<h1>邮件发送可以吗？</h1>'

    # 加载
    index = loader.get_template('axf/user/register/active.html')
    # 渲染
    context={
        'name':'顺利',
        'url':'http://www.my6767.com/pro_18539982.html'
    }
    result = index.render(context=context)
    html_message = result

    # 发送者
    from_email='yulin_ljing@163.com'
    # 接收者
    recipient_list=['yulin_ljing@163.com']

    send_mail(subject=subject,message=message,html_message=html_message,from_email=from_email,recipient_list=recipient_list)

    return HttpResponse('邮件发送成功')


def account(request):

    # 127.0.0.1：8000/axfuser/account?token=fdfdshfdfkdhfkhdkjfhdkjfhkdjhf
    # 将当前注册的用户的激活状态修改为True
    # token就是代表的是当前对象的token
    token = request.GET.get('token')
    user_id = cache.get(token)

    if user_id:
        user = AxfUser.objects.get(pk=user_id)
        user.active = True
        user.save()
        # 删除缓存的方法没有任何的提示  是delete方法   *********************
        cache.delete(token)
        return HttpResponse('激活成功')
    else:
        return HttpResponse('邮件已过期')






    # users = AxfUser.objects.filter(token=token)
    #
    # if users.count() > 0:
    #     user = users.first()
    #     user.active = True
    #
    #     user.save()
    #     return HttpResponse('激活成功')

def get_code(request):
    # 初始化画布，初始化画笔

    mode = "RGB"

    size = (200, 100)

    red = get_color()

    green = get_color()

    blue = get_color()

    color_bg = (red, green, blue)
    # 导包的时候  你导入的PIL下的Image的image
    # from PIL.Image import Image
    image = Image.new(mode=mode, size=size, color=color_bg)

    imagedraw = ImageDraw(image, mode=mode)
    # FONT_PATH 验证码的字体
    imagefont = ImageFont.truetype(settings.FONT_PATH, 100)

    verify_code = generate_code()

    request.session['verify_code'] = verify_code

    for i in range(4):
        fill = (get_color(), get_color(), get_color())
        imagedraw.text(xy=(50*i, 0), text=verify_code[i], font=imagefont, fill=fill)

    for i in range(100):
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