import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

#sender发件人，password服务器授权码， mail_host 服务器地址（QQsmtp） receiver接收者
sender = '1193685537@qq.com'
password = '####'
mail_host = 'smtp.qq.com'
receives = ['daacheng@sina.cn','luzhicheng@wiscosoft.com.cn','baolu@wiscosoft.com.cn']

#设置邮件信息
msg = MIMEMultipart()

#邮件主题
msg['Subject'] = input("请输入邮件主题: ")

msg['From'] = sender

msg_content = input("请输入正文：")

msg.attach(MIMEText(msg_content,'plain','utf-8'))

#登录并发送
try:
	s = smtplib.SMTP_SSL("smtp.qq.com", 465)
	s.set_debuglevel(1)
	s.login(sender, password)
	#给接收者发送消息
	for i in range(len(receives)):
		to = receives[i]
		msg['To'] = to
		s.sendmail(sender, to, msg.as_string())
		print('success!')

	s.quit()
	print('All email has been send over')
except smtplib.SMTPException as e:
	print("Failed ,%s",e)