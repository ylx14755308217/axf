from django.conf.urls import url

from CartApp import views

urlpatterns =[
    url(r'^cart/',views.cart,name='cart'),

    url(r'^addToCart/',views.addToCart,name='addToCart'),
]