from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from CartApp.models import AxfCart
from MarketApp.models import AxfGoods
from UserApp.models import AxfUser


def cart(request):

    # 购物车中的数据 应该展示的是当前登陆的用户的数据
    user_id = request.session.get('user_id')
    # 没有登陆 就不允许进入到购物车  未登陆将进入到登陆页面
    if user_id:
        user = AxfUser.objects.get(pk=user_id)
        cart = AxfCart.objects.filter(c_user=user)

        # cart = AxfCart.objects.filter(c_user_id=user_id)
        context = {
            'cart':cart
        }
        return render(request,'axf/main/cart/cart.html',context=context)
    else:
        return  redirect(reverse('axfuser:login'))


def addToCart(request):
    data = {
        'status':200,
        'msg':'ok',
    }
    user_id = request.session.get('user_id')

    if user_id:
        user = AxfUser.objects.get(pk=user_id)
        goodsid = request.GET.get('goodsid')
        goods = AxfGoods.objects.get(pk=goodsid)

        carts = AxfCart.objects.filter(c_user=user).filter(c_goods=goods)

        if carts.count() > 0:
            cart = carts.first()
            cart.c_goods_num = cart.c_goods_num + 1
        else:
            cart = AxfCart()
            cart.c_user = user
            cart.c_goods = goods
        cart.save()

        data['c_goods_num']=cart.c_goods_num

        return JsonResponse(data=data)
    else:
        data['status'] = 201
        data['msg']='用户未登陆'
        return JsonResponse(data=data)

