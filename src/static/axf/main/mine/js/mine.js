$(function(){
    $('#regis').click(function () {
    //    跳转到登陆页面
    //     window.location.href = '/axfuser/register/';
        window.open('/axfuser/register/',target='_self');
    })

    $('#login').click(function () {
        window.location.href = '/axfuser/login/';
    })
})