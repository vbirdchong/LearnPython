#!/env/usr/bin python
# coding=utf-8

import smtplib
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

# def send_mail(to_list, sub, content):
# 	me = 'hello' + '<' + mail_user + '@' + mail_postfix + '>'
# 	msg = MIMEText(content, _subtype = 'plain', _charset='utf-8')
# 	msg['Subject'] = sub
# 	msg['From'] = me
# 	msg['To'] = ';'.join(to_list)
# 	msg['Data'] = formatdate(localtime=True)

# 	try:
# 		server = smtplib.SMTP()
# 		server.connect(mail_host)
# 		server.login(mail_user, mail_pass)
# 		server.sendmail(me, to_list, msg.as_string())
# 		server.close()
# 		return True
# 	except Exception, e:
# 		print str(e)
# 		return False

# server{'name':xx, 'user':xxx, 'password':xxx}
def send_mail(server, fro, to, subject, content, files=[]):
	assert type(server) == dict
	assert type(to) == list
	assert type(files) == list

	print files

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

	try:
		smtp = smtplib.SMTP(server['name'])
		smtp.login(server['user'], server['password'])
		smtp.sendmail(fro, to, msg.as_string())
		smtp.close()
		return True
	except Exception, e:
		print str(e)
		return False


if __name__ == '__main__':
	server = {'name':'smtp.163.com', 'user':'xxx@163.com', 'password':'xxx'}
	fro = 'CC_python' + '<' + server['user'] + '@' + 'cc_python.com' + '>'
	to = ['xxx@163.com']
	subject = 'AQI_PM25 record'
	content = 'new data will be update'
	files = ['img1.png']

	if send_mail(server, fro, to, subject, content, files):
	# if send_mail(mail_to_list, 'hello python', 'send mail by python'):
		print 'send success...'
	else:
		print 'send fail...'