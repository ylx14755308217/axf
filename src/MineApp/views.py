from django.shortcuts import render

# Create your views here.
from UserApp.models import AxfUser


def mine(request):
    # 登陆的试图函数重定向到mine的视图
    # 图片和姓名都应该是登陆的哪个用户
    user_id = request.session.get('user_id')
    if user_id:
        user = AxfUser.objects.get(pk=user_id)
        context = {
            'user':user
        }
        return render(request,'axf/main/mine/mine.html',context=context)
    else:
        return render(request,'axf/main/mine/mine.html')
