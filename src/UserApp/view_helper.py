from django.core.mail import send_mail
from django.template import loader

from axf.settings import EMAIL_HOST_USER


def sendEmail(name,email,token):
    subject = '胡辰月是小猪'
    message = ''
    index = loader.get_template('axf/user/register/active.html')

    # 渲染
    context = {
        'name':name,
        # url 应该是一个请求资源路径 专门用来修改对象的激活状态
        'url':'http://47.103.147.46:8000/axfuser/account/?token='+str(token)
    }
    result = index.render(context=context)

    html_message = result

    from_email = EMAIL_HOST_USER
    # 发件人
    recipient_list = [email]
    # 接收者
    send_mail(subject=subject, message=message, html_message=html_message, from_email=from_email,
              recipient_list=recipient_list)