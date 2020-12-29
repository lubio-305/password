while True:
	password = input('請輸入密碼: ')
	if password == 'a123456':
		break
		print('登入成功')
	elif password != 'a123456':
		print('最多輸入3次密碼')
		if password == 'a123456':
			break
			print('登入成功')
		elif password != 'a123456':
			print('密碼錯誤!還有2次機會')
			if password == 'a123456':
				break
				print('登入成功')
			elif password != 'a123456':
				print('密碼錯誤!還有1次機會')
				if password == 'a123456':
					break
					print('登入成功')
				elif password != 'a123456':
					break
					print('密碼錯誤!帳號已鎖定')


			


