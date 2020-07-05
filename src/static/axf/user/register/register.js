$(function () {
    $('#exampleInputName').blur(function () {
        //获取文本中内容
        var name = $(this).val();
        //定义正则
        var reg = /^[a-z]{3,8}$/;
        //判断内容是否符合正则
        var b = reg.test(name);
        //如果符合提示可以  绿色字体
        //如果不符合提示用户名字必须是3到6个英文字母 红色字体
        if(b){
            $('#nameinfo').html('用户名字可以使用').css('color','green');
        }else{
            $('#nameinfo').html('3到8个英文字母').css('color','red');
        }
    })
})