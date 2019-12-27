country = input('請輸入您的國家：')
age = input('請輸入您的年齡：')
age = int(age)
if country == '日本':
	if age >= 18:
		print('你可以考駕照了喔')
	else:
		print('你還不能考駕照喔')
elif country == '美國':
	if age >= 16:
		print('你可以考駕照了喔')
	else:
		print('你還不能考駕照喔')
else:
	print('只能輸入日本或美國')