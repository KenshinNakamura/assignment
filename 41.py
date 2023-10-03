#41 1桁の自然数?
#整数値を入力させ、その値が一桁の自然数かそうでないか判定するプログラムを作成せよ。

num1 = int(input("要素番号を入力してください: "))
print(f"input number :" , num1)

if num1 > 0 and num1 < 10:
    print("一桁の自然数である")

else:
    print("一桁の自然数ではない")