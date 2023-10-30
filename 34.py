#34 入力値抜き改
#整数値を入力させ、1から9まで、入力値と入力値+1以外を表示するプログラムを作成せよ。
#入力値が9の場合は9のみ表示しない。

num = int(input("整数値を入力してください: "))
print(f"input number :" , num)

for i in range(1, 10):
    if i == num or i == num + 1:
        continue
    print(i)