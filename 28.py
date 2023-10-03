# 28 nの階乗
#整数値を入力させ、その値の階乗を表示するプログラムを作成せよ。
#ただし、0以下の値を入力した場合は1と表示する。


    # 整数値を入力させる
num = int(input("整数値を入力してください: "))
print(f"input number :" , num)

    # 階乗を計算
if num <= 0:
        factorial = 1
else:
        factorial = 1
        for i in range(1, num + 1):
            factorial *= i
    
print(f"{num}の階乗は: {factorial}")
