#32 5の倍数でbar
#1から20まで順に表示するが、5の倍数の場合は数字の代わりにbarと表示するプログラムを作成せよ。


i = 1
while i <= 20:
    if i % 5 == 0:
        print("bar")
    else:
        print(i)
    i += 1


