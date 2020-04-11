#密碼重試程式
#密碼是＝a123456
#最多輸入三次密碼
#錯誤會印出 ”密碼錯誤，還剩ＸＸ次幾會“ 對的話印出 “登入成功”

while True:
	password = input('please enter your password :')
	if password == 'a123456' :
		print('successful login!')
		break
	elif password != 'a123456' :
		print('wrong!you still have two times to try~')
		input('please enter your password :')
		if password != 'a123456' :
			print('wrong! this is final attempt ~ ')
			input('please enter your password :')
			if password != 'a123456':
				print('no chance , lock in!')
				break




