//   标签对象。事件（function（）{}）
//事件   click blur change  keyup submit

//$(this)代表的是当前的点击对象$('#all_type')
//toggleClass() 会将2个样式进行交互替换

$(function () {
    $('#all_type').click(function () {
        $(this).find('span').toggleClass('glyphicon glyphicon-chevron-down glyphicon glyphicon-chevron-up');
        $('#all_type_container').toggle();
    })
    
    $('#sort_rule').click(function () {
        $(this).find('span').toggleClass('glyphicon glyphicon-chevron-down glyphicon glyphicon-chevron-up')
        $('#sort_rule_container').toggle();
    })


    $('.addToCart').click(function () {

        var $button = $(this);

        var goodsid = $button.attr('goodsid');

        $.get('/axfcart/addToCart/',
             {'goodsid':goodsid},
             function (data) {
                 if(data['status'] == 200){
                     $button.prev().html(data['c_goods_num']);
                 }else{
                     window.location.href='/axfuser/login/';
                 }
             })









    //    prop和attr都是获取标签属性的方法
    //    prop和attr都可以获取标签自带的属性值
    //    prop不可以获取标签自定义的属性值
    //    获取goodsid
    //     var goodsid = $(this).attr('goodsid');
    //     alert(goodsid);

        // var a = $(this).prop('goodsid');
        // alert(a);







    //    将商品添加到购物车中
    //    购物车需要哪些必须的数据
    //    c_user c_goods
    //    c_user 可以通过session来获取
    //    c_goods
    })



})