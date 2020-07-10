from django.shortcuts import render

# Create your views here.
from MarketApp.models import AxfFoodType, AxfGoods
from MarketApp.view_constant import COMP_SORT_RULE, ORDER_BY_PRICE_UP, ORDER_BY_PRICE_DOWN, ORDER_BY_PRODUCTNUM_UP, \
    ORDER_BY_PRODUCTNUM_DOWN


def market(request):
    # 左栏
    foodtypes = AxfFoodType.objects.all()


    # 右上   分类显示
    typeid = request.GET.get('typeid','104749')

    childtypenames = AxfFoodType.objects.filter(typeid=typeid)[0].childtypenames
    # 全部分类:0#酸奶乳酸菌:103537#牛奶豆浆:103538#面包蛋糕:103540
    # print(childtypenames)
    childtypename_list = childtypenames.split('#')
    # ['全部分类:0', '酸奶乳酸菌:103537', '牛奶豆浆:103538', '面包蛋糕:103540']
    # print(childtypename_list)
    c_list = []

    for childtypename in childtypename_list:
        # 面包蛋糕和103540是在页面中都必须要使用
        # ['酸奶乳酸菌', '103537']
        c = childtypename.split(':')
        c_list.append(c)

    # [['全部分类', '0'], ['酸奶乳酸菌', '103537'], ['牛奶豆浆', '103538'], ['面包蛋糕', '103540']]
    # print(c_list)

    # 商品数据展示
    # foodtype的typeid 和 goods的categoryid一致
    goods_list = AxfGoods.objects.filter(categoryid=typeid)

    childcid = request.GET.get('childcid','0')

    # 如果是第一次跳转到这个视图函数  那么是没有childcid的 所有就是查询的所有
    if childcid == '0':
        goods_list = goods_list
    else:
        goods_list = goods_list.filter(childcid=childcid)


    # 排序分类展示
    sort_rule_list = [
        ['综合排序',COMP_SORT_RULE],
        ['价格升序',ORDER_BY_PRICE_UP],
        ['价格降序',ORDER_BY_PRICE_DOWN],
        ['销量升序',ORDER_BY_PRODUCTNUM_UP],
        ['销量降序',ORDER_BY_PRODUCTNUM_DOWN],
    ]

    s_rule = request.GET.get('s_rule','0')

    if s_rule == COMP_SORT_RULE:
        pass
    elif s_rule == ORDER_BY_PRICE_UP:
        goods_list = goods_list.order_by('price')
    elif s_rule == ORDER_BY_PRICE_DOWN:
        goods_list = goods_list.order_by('-price')
    elif s_rule == ORDER_BY_PRODUCTNUM_UP:
        goods_list = goods_list.order_by('productnum')
    elif s_rule == ORDER_BY_PRODUCTNUM_DOWN:
        goods_list = goods_list.order_by('-productnum')


    context = {
        'foodtypes':foodtypes,
        'goods_list':goods_list,
        'typeid':typeid,
        'c_list':c_list,
        'childcid':childcid,
        'sort_rule_list':sort_rule_list,
        's_rule':s_rule,
    }

    return render(request,'axf/main/market/market.html',context=context)