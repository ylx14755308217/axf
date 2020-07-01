from django.conf.urls import url

from AxfHome import views

urlpatterns = [

    url(r'^home/',views.home,name='home'),

]