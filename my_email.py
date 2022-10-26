# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     email
   Author :       chenci
   date：          2022/10/25
-------------------------------------------------
"""

import yagmail

sender_email = ''  # 发件人地址 必填
sender_pass = ''  # 邮件授权码   必填
receiver_mail = ''  # 收件人邮箱 必填
title = '叮~ 漏洞扫描推送'  # 邮件主题


# 发送邮件
def send_mail(run_time):
    try:
        yagmail.SMTP(user=sender_email, password=sender_pass, host='smtp.qq.com', port=465).send(to=receiver_mail,
                                                                                                 subject=title,
                                                                                                 contents=f'漏洞扫描已完成!\n耗时:{run_time}')
        print('邮件已发送!')
    except Exception as e:
        print(e)
