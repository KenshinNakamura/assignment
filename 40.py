#40 even or odd
#整数値を入力させ、その値が偶数ならばeven、奇数ならばoddと表示するプログラムを作成せよ。

num1 = int(input("要素番号を入力してください: "))

if num1 % 2 == 0:
    print("even")

else:
    print("odd")