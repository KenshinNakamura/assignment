#27 1からnまでの和
#整数値を入力させ、1からその値までの総和を計算して表示するプログラムを作成せよ。
#ただし、0以下の値を入力した場合は0と表示する。

    # 整数値を入力させる
num = int(input("整数値を入力してください: "))
total = 0

if num <= 0:
    total = 0
else:
    i = 1
    while i <= num:
        total += i
        i += 1

print("総和:", total)

