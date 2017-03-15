#! /usr/bin/env python
# -*- coding=utf-8 -*-

# usage: python email_163.py <attachment file name>

import smtplib
import sys
import re

from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email import encoders
from email.utils import COMMASPACE, formatdate

mail_to_list = ['xxxx@163.com']
mail_host = 'smtp.163.com'
mail_user = 'xxxx.com'
mail_pass = 'xxxx'
mail_postfix = 'pyhon_aqi_record.com'


def send_mail(server, fro, to, subject, content, files=[]):
    assert type(server) == dict
    assert type(to) == list
    assert type(files) == list

    # print files

    msg = MIMEMultipart()
    msg['From'] = fro
    msg['To'] = COMMASPACE.join(to)
    msg['Subject'] = subject
    msg['Data'] = formatdate(localtime=True)

    # 邮件正文
    msg.attach(MIMEText(content, 'plain', 'utf-8'))

    # 这里主要添加的是以图片形式的附件,默认以PNG形式的图片
    for file in files:
        print 'file-->'
        print file
        with open(file, 'rb') as fp:
            # 如果使用MIMEImage 方式来添加图片附件，则只要这一步就可以完成，不必添加头信息，但需要图片是PNG格式
            img = MIMEImage(fp.read())

            # 如果使用MIMEBase 方式来添加图片附件，并且可以给附件命名，更加灵活一些，则以下的步骤不可少
            # img = MIMEBase('image', 'png', filename=file)
            # # 添加必要的头信息，否则会在邮件箱里出现图片预览失败，也就是说图片没有传成功
            # img.add_header('Content-Disposition', 'attachment', filename=file)
            # img.add_header('Content-ID', '<0>')
            # img.add_header('X-Attachment-Id', '0')
            # img.set_payload(fp.read())
            # encoders.encode_base64(img)

            # 作为附件的一部分继续添加进去
            msg.attach(img)

    # try:
    #     smtp = smtplib.SMTP(server['name'])
    #     smtp.login(server['user'], server['password'])
    #     smtp.sendmail(fro, to, msg.as_string())
    #     smtp.close()
    #     return True
    # except Exception, e:
    #     print str(e)
    #     return False


def main():
    server = {'name': 'smtp.163.com', 'user': 'xxx@163.com', 'password': 'xxx'}
    fro = 'CC_python' + '<' + server['user'] + '@' + 'cc_python.com' + '>'
    to = ['xxx@163.com']

    if len(sys.argv) == 2:
        comment = re.compile('(.*)(\.)(.*)')
        subject = comment.search(sys.argv[1]).group(1)
        content = subject + 'file added'
        files = [sys.argv[1]]
    else:
        subject = 'Test'
        content = 'new data will be update'

    print(subject)

    if send_mail(server, fro, to, subject, content, files):
        print 'send success...'
    else:
        print 'send fail...'


if __name__ == '__main__':
    main()
