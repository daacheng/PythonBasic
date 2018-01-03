error_num=0
while True:
	username=input('please input username:')
	password=input('please input password:')
	if username=='daacheng' and password=='daacheng':
		print('successful')
	else:
		print('faile')
		error_num+=1
		if  error_num==3:
			exit()
		else:
			print('last input ',3-error_num)
			continue