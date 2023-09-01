password = 'a123456'
n = 3
while True:
	try_password = input('请输入密码: ')
	if try_password == password:
		print('登入成功')
		raise SystemExit  #用break或许更好
	else:
		print('密码错误,你还有 ',n - 1 ,'次机会')
		n -= 1
		if n == 0:
			print('密码错误已达到上限')
			raise SystemExit  #用break或许更好

