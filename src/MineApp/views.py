from django.shortcuts import render

# Create your views here.

# 登陆的视图函数重定向到mine的视图
# 图片和姓名都应该是登陆的那个用户的数据

# 问题：就是登陆的那个对象  怎么放到mine的视图函数
from UserApp.models import AxfUser


def mine(request):

    user_id = request.session.get('user_id')

    if user_id:
        print(1111111)
        # get方法获取不到对象的时候  就会报错   matching query does not exist.
        user = AxfUser.objects.get(pk=user_id)

        context = {
            'user1':user
        }

        return render(request,'axf/main/mine/mine.html',context=context)
    else:
        # centos操作系统上  django的模板中user 是有一个默认值的   所以不允许使用user变量
        # ubuntu操作系统上  django的模板中user 是没有默认值的
        return render(request,'axf/main/mine/mine.html')
