#18 配列を入力値で初期化
#要素数10の整数型の配列を宣言し、整数値を入力させ、すべての配列の要素を入力値として、すべての要素の値を表示するプログラムを作成せよ。

# 整数型のリストを宣言し、各要素を初期化
array = [i for i in range(10)]

# リストの要素を順に表示
for i in range(10):
    print(f"array[{i}] = {array[i]}")