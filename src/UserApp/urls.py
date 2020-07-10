from django.conf.urls import url

from UserApp import views

urlpatterns=[
    url(r'^register/',views.register,name='register'),
    url(r'^login/',views.login,name='login'),

#     用户名字的后台验证
    url(r'^checkName/',views.checkName,name='checkName'),

#     发送邮件
    url(r'^testEmail/',views.testEmail),

#   http  https
#     https =  http + ssl
#      ssl 安全 套接层  安全
#     激活
    url(r'^account/',views.account),

#     验证码
    url(r'^get_code/',views.get_code),

#     退出
    url(r'^logout/',views.logout,name='logout'),
]