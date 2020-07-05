from django.conf.urls import url

from UserApp import views

urlpatterns=[
    url(r'^register/',views.register,name='register'),

    url(r'^login/',views.login,name='login'),
]