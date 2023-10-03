#29 5つの合計
#整数値を5回入力させ、それらの値の合計を表示するプログラムを繰り返しを使って作成せよ。

total = 0  # 合計を初期化

for _ in range(5):  # 5回繰り返す
        num = int(input("整数値を入力してください: "))
        total += num  # 合計に入力値を加える
print(f"input number :" , num)
print("入力された整数値の合計は:", total)
