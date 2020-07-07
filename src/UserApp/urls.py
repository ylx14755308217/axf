from django.conf.urls import url

from UserApp import views

urlpatterns=[
    url(r'^register/',views.register,name='register'),

    url(r'^login/',views.login,name='login'),

    url(r'^checkName/',views.checkName,name='checkName'),

    url(r'^account/',views.account,name='account'),

# 验证码
    url(r'^get_code/',views.get_code,name='get_code'),

    url(r'^logout/',views.logout,name='logout')
]