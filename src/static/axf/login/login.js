$(function () {
    $('#changeImage').click(function () {
        // 给img标签的src的属性重新赋值
        // 浏览器有一个缓存问题 当页面中有请求重复提交 服务器以为误操作
        // 所以不允许提交
        $(this).attr('src','/axfuser/get_code/?'+Math.random());
    })
    $('form').submit(function () {
        var password = $('#exampleInputPassword1').val();
        $('#exampleInputPassword1').val(md5(password));
        return true;
    })
})
