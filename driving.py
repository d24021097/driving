contry = input('請輸入您的國家：')
age = input('請輸入您的年齡：')
age = int(age)
if contry == '日本':
	if age >= 18:
		print('你可以考駕照了喔')
	else:
		print('你還不能考駕照喔')