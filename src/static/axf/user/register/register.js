$(function () {

    var flagname = false;

    var flagpassword = false;

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
            //$('#nameinfo').html('用户名字可以使用').css('color','green');
            //会执行请求 然后将这个用户名字 传到视图函数中
            //视图函数 去数据库验证是否有这个数据
            $.getJSON('/axfuser/checkName/',
                        {'name':name},
                function (data) {
                    if(data['status'] == 200){
                        $('#nameinfo').html(data['msg']).css('color','green');
                        flagname = true;
                    }else{
                        $('#nameinfo').html(data['msg']).css('color','red');
                    }
                }
                )
        }else{
            $('#nameinfo').html('3到8个英文字母').css('color','red');
        }
    })

    $('#exampleInputPassword2').blur(function () {
        var password = $('#exampleInputPassword1').val();
        var password2 = $('#exampleInputPassword2').val();
        if(password==password2) {
            $('#passwordinfo').html('密码一致').css('color', 'green');
            flagpassword = true;
        }else{
            $('#passwordinfo').html('密码不一致').css('color', 'red');
        }
    })


    $('form').submit(function (){
        var name = $('#exampleInputName').val();
        if (!name){
            $('#nameinfo').html('用户名字不能为空').css('color','red');
        }
        var password = $('#exampleInputPassword1').val();
        if(!password){
            $('#passwordinfo').html('密码不能为空').css('color','red');
            return false;
        }
// 只有所有验证都通过之后 才会提交表单
        //  false & true  之间的关系
        var b = flagname & flagpassword;

        if(b == 1){
    // 加密之后的密码
            password = md5(password);
                //将加密的密码重新赋值给文本框
            $('#exampleInputPassword1').val(password);
            return true;
        }else{
        return false;
        }
    })

})