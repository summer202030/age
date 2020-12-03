driving = input("請問你有沒有開過車?")
if driving != "有" and driving != "沒有" :
	print("只能輸入 有/沒有")
	raise SystemExit #程式到此終止

age = input("請問你的年齡?")
age = int(age)
if driving == "有":
	if age >= 18: #如果有達到條件，深一層部分需要前方有空格在輸入下一個如果
		print("你通過測驗了")
	else:
		print("奇怪!你怎麼會開過車")
elif driving == "沒有":
	if age >= 18:
		print("你可以考駕照了哦，怎麼還不去考呢?")
	else:
		print("很好，再過幾年就可以考駕照了")
else:
	print("只能輸入 有/沒有")
