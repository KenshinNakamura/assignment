#27 1からnまでの和
#整数値を入力させ、1からその値までの総和を計算して表示するプログラムを作成せよ。
#ただし、0以下の値を入力した場合は0と表示する。

num = int(input("整数値を入力してください: "))
total = 0

if num <= 0:
    total = 0
else:
    i = 1
    for i in range(1, num + 1):
        total += i

print("総和:", total)

