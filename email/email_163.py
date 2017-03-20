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
from email.mime.application import MIMEApplication
from email import encoders
from email.utils import COMMASPACE, formatdate


def send_mail(server, fro, to, subject, content, files=[]):
    assert type(server) == dict
    assert type(to) == list
    assert type(files) == list

    msg = MIMEMultipart()
    msg['From'] = fro
    msg['To'] = COMMASPACE.join(to)
    msg['Subject'] = subject
    msg['Data'] = formatdate(localtime=True)

    print('Subject info: ' + subject)

    # 邮件正文
    # msg.attach(MIMEText(content, 'plain', 'utf-8'))

    # 这里主要添加的是以图片形式的附件,默认以PNG形式的图片
    for file in files:
        print ('find file -->' + file)

        if file[-3:] == 'png' or file[-3:] == 'jpg':
            with open(file, 'rb') as fp:
                # 如果使用MIMEImage 方式来添加图片附件，则只要这一步就可以完成，不必添加头信息，但需要图片是PNG格式
                img = MIMEImage(fp.read())

                # 作为附件的一部分继续添加进去
                msg.attach(img)
                print('adding image -->' + file)
        elif file[-3:] == 'txt':
            txtFile = MIMEApplication(open(file, 'rb').read())
            txtFile.add_header('Content-Disposition', 'attachment', filename=file)
            msg.attach(txtFile)
            print('adding \'txt\' file -->' + file)

    try:
        smtp = smtplib.SMTP(server['name'])
        smtp.login(server['user'], server['password'])
        smtp.sendmail(fro, to, msg.as_string())
        smtp.close()
        return True
    except Exception, e:
        print str(e)
        return False


def main():
    server = {'name': 'smtp.163.com', 'user': 'xxx@163.com', 'password': 'xxx'}
    fro = 'CC_python' + '<' + server['user'] + '>'
    to = ['xxx@163.com', 'xxx@kindle.cn']

    if len(sys.argv) == 2:
        comment = re.compile('(.*)(\.)(.*)')
        subject = comment.search(sys.argv[1]).group(1)
        content = subject
        files = [sys.argv[1]]
    else:
        subject = 'Test'
        content = 'Send from python script'

    if send_mail(server, fro, to, subject, content, files):
        print 'send success...'
    else:
        print 'send fail...'


if __name__ == '__main__':
    main()
