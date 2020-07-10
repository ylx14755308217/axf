$(function () {
    var flagname = false;
    var flagpassword = false;


    $('#exampleInputName').blur(function () {
    //    获取文本框中的内容
        var name = $(this).val();
    //    定义一个正则
        var reg = /^[a-z]{3,8}$/;
    //    判断内容是否符合正则  test方法
    // 如果name符合reg的要求就返回true  如果不符合要求就返回false
        var b = reg.test(name);
    //    如果符合提示可以  绿色字体
    //    如果不符合提交用户名字必须是3到6个英文字母  红色字体
        if(b){
            // $('#nameinfo').html('用户名字可以使用').css('color','green');
            // 会执行请求 然后将这个用户名字 传到视图函数中
            // 视图函数 去数据库验证是否有这个数据 如果有  那么提示用户名字已经注册
            // 如果没有 那么显示用户名字可以使用
            // $.getJson  $.get   $.post  $.ajax
            // getJSON(请求资源路径，请求参数，执行完请求之后获取的值)
            //data 就是服务器响应的数据  json数据  注意一定是json
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

        var passwrod2 = $('#exampleInputPassword2').val();

        if(password == passwrod2){
            $('#passwordinfo').html('密码一致').css('color','green');
            flagpassword =true;
        }else{
            $('#passwordinfo').html('密码不一致').css('color','red');
        }
    })
    
    // submit方法中  只有返回true才可以提交表单  如果返回false那么就不允许提交
    $('form').submit(function () {


        var name = $('#exampleInputName').val();
        if(!name){
            $('#nameinfo').html('用户名字不能为空').css('color','red');
        }

        var password = $('#exampleInputPassword1').val();
        if(!password){
            $('#passwordinfo').html('密码不能为空').css('color','red');
            return false;
        }

    //    只有所有的验证都通过之后  才会提交表单
    //     false  0   true  1
        //false & false  == > 0     0 * 0
        //false & true   ==>  0     0 * 1
        //true & true  == >  1      1 * 1

        var b = flagname & flagpassword;

        if(b == 1){
            //加密之后的密码
            password = md5(password);
            //将加密的密码重新赋值给文本框
            $('#exampleInputPassword1').val(password);
            return true;
        }else{
            return false;
        }


    })



})