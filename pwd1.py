#密碼重試程式
#密碼是＝a123456
#最多輸入三次密碼
#錯誤會印出 ”密碼錯誤，還剩ＸＸ次幾會“ 對的話印出 “登入成功”

password = 'a123456'
c = 3 #剩餘機會

while True :
	pwd = input('please enter your password :')
	if pwd == password :
		print('successful logined')
		break
	else :
		c = c - 1
		print('wrong! still have', c , 'times !')
		if c == 0 :
			print('no chance!')
			break