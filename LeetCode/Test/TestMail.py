# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr


my_sender = 'wangyn@qeek.cc'
my_pass = 'QoNEba5J4Bn9yBJp'
my_user = 'mobile@qeebike.com'


def mail():
    ret = True

    try:
        msg = MIMEText('Python mail test', 'plain', 'utf-8')
        msg['From'] = formataddr(['iOS开发', my_sender])
        msg['To'] = formataddr(['骑迹', my_user])
        msg['Subject'] = 'Python测试邮件'

        server = smtplib.SMTP_SSL("smtp.exmail.qq.com", 465)
        server.login(my_sender, my_pass)
        server.sendmail(my_sender, [my_user, ], msg.as_string())

        server.quit()
    except Exception:
        ret = False

    return ret


ret = mail()

if ret:
    print('邮件发送成功')
else:
    print("邮件发送失败")
