#15 2ずつカウントアップ
#整数値を入力させ、0から入力値を超えない値まで2ずつ増やして表示するプログラムを作成せよ。
num = int(input("整数値を入力してください:"))
print(f"input number :" , num)
for i in range(0, num + 1, 2):
        print(i)