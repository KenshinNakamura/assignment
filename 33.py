#33 入力値抜き
#整数値を入力させ、1から9まで、入力値以外を表示するプログラムを作成せよ。


num = int(input("整数値を入力してください: ")) 

for i in range(1, 10):
    if i  != num:
        print(i)