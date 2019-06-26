country = input('请输入国家:' )
age = input('请输入年龄:' )
age = int(age)
if country == '中国':
	if age >= 18:
		print('你可以考驾照')
		else:
		print('你不可以考驾照') 
