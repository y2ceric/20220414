import random

r = random.randint(1, 100)
while True:
	x = int(input("請輸入整數(1~100):"))
	if x == r:
		break
	elif x > r:
		print("比答案大")
	else:
		print("比答案小")
print("猜中了!")