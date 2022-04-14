password = "a12345"
count = 0
while count < 3:
	pwd = input("請輸入密碼")
	if pwd == password:
		print("密碼正確")
		break
	else:
		count = count + 1
		print("密碼錯誤!")
		if count < 3:
			print("還有", 3 - count, "次機會!")