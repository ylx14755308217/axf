from django.shortcuts import render

# Create your views here.
from MarketApp.models import AxfFoodType, AxfGoods
from MarketApp.views_constant import COMP_SORT_RULE, COMP_BY_PRICE_UP, COMP_BY_PRICE_DOWN, COMP_BY_PRODUCTNUM_UP, \
    COMP_BY_PRODUCTNUM_DOWN


def market(request):

    foodtypes = AxfFoodType.objects.all()

    typeid = request.GET.get('typeid','104749')

    childtypenames = AxfFoodType.objects.filter(typeid=typeid)[0].childtypenames

    childtypename_list = childtypenames.split('#')
    c_list = []
    for childtypename in childtypename_list:
        c = childtypename.split(':')
        c_list.append(c)

# 商品数据的展示
#  foodtype的typeid 和 goods的categoryid一致
    goods_list =AxfGoods.objects.filter(categoryid=typeid)

    childcid =request.GET.get('childcid','0')

#如果是第一次跳转到这个视图函数 那么没有childid的 所有就是查询的所有
    if childcid == '0':
        goods_list = goods_list
    else:
        goods_list = goods_list.filter(childcid=childcid)


# 排序分类展示
    sort_rule_list = [
        ['综合排序',COMP_SORT_RULE],
        ['价格升序',COMP_BY_PRICE_UP],
        ['价格降序',COMP_BY_PRICE_DOWN],
        ['销量升序',COMP_BY_PRODUCTNUM_UP],
        ['销量降序',COMP_BY_PRODUCTNUM_DOWN],
]
    s_rule =request.GET.get('s_rule','0')
    if s_rule == COMP_SORT_RULE:
        pass
    elif s_rule == COMP_BY_PRICE_UP:
        goods_list =goods_list.order_by('price')
    elif s_rule == COMP_BY_PRICE_DOWN:
        goods_list = goods_list.order_by('-price')
    elif s_rule == COMP_BY_PRODUCTNUM_UP:
        goods_list = goods_list.order_by('productnum')
    elif s_rule == COMP_BY_PRODUCTNUM_DOWN:
        goods_list = goods_list.order_by('-productnum')


    context = {
        'foodtypes':foodtypes,
        'goods_list':goods_list,
        'typeid':typeid,
        'c_list':c_list,
        'childcid':childcid,
        'sort_rule_list':sort_rule_list,
        's_rule':s_rule
    }
    return render(request,'axf/main/market/market.html',context=context)