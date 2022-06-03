#產生一個隨機整數1~100 (不要印出來)
#讓使用者重複書速數字去猜
#猜對的話 印出 "終於猜對了"
#猜錯的話 要告訴他 比答案大/小

import random
count = 0
r = random.randint(1, 100)
while True:
	count += 1 #count = count + 1
	num = input('請猜數字: ')
	num = int(num)
	if r == num:
		print('你猜中了!')
		print('你總共猜了', count, '次')
		break
	elif r > num:
		print('比答案小')
	elif r < num:
		print('比答案大')
	print('這是你猜的第', count, '次')