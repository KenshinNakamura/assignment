#35 配列要素の参照
#{3, 7, 0, 8, 4, 1, 9, 6, 5, 2}で初期化される大きさ10の整数型配列を宣言し、
#整数値を入力させ、要素番号が入力値である配列要素の値を表示するプログラムを作成せよ。
# 入力値が配列の要素の範囲外であるかどうかのチェックは省略してよい。

num = int(input("整数値を入力してください: "))
print(f"input number :" , num)

# 配列を初期化
array = [3, 7, 0, 8, 4, 1, 9, 6, 5, 2]

# 入力値が配列の要素番号として適切かどうかのチェックは省略しています

# 配列要素の値を表示
if 0 <= num < len(array): #len(array)はデータの長さ(10)
    print(f"array[{num}] = {array[num]}" )
