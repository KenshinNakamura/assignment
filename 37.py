#37 続々・配列要素の参照
#{3, 7, 0, 8, 4, 1, 9, 6, 5, 2}で初期化される大きさ10の整数型配列を宣言し、
#整数値を入力させ、要素番号が入力値の配列要素の値を参照し
#さらにその参照した値を要素番号とする配列要素の値を参照して表示するプログラムを作成せよ。
#入力値が配列の要素の範囲外であるかどうかのチェックは省略してよい。

array = [3, 7, 0, 8, 4, 1, 9, 6, 5, 2]

num1 = int(input("要素番号を入力してください: "))

if 0 <= num1 <= len(array):
    index1 = array[num1]
    if 0 <= index1 <= len(array):
        result = array[index1] 
    print(f"input number : {num1}")
    print(f"value = {result}")
