#36 続・配列要素の参照
#{3, 7, 0, 8, 4, 1, 9, 6, 5, 2}で初期化される大きさ10の整数型配列を宣言し、
#整数値を2つ入力させ、要素番号が入力値である2つの配列要素の値の積を計算して表示するプログラムを作成せよ。
#入力値が配列の要素の範囲外であるかどうかのチェックは省略してよい。

num1 = int(input("一つ目の整数値を入力してください: "))
num2 = int(input("二つ目の整数値を入力してください: "))
print(f"input number :" , num1)
print(f"input number :" , num2)

# 配列を初期化
array = [3, 7, 0, 8, 4, 1, 9, 6, 5, 2]

# 入力値が配列の要素番号として適切かどうかのチェックは省略しています

# 配列要素の値を表示
if 0 <= num1 < len(array) and 0 <= num2 < len(array):
    num_result = array[num1] * array[num2]

    print("要素番号", num1, "と要素番号" , num2 , "の値は", 
          array[num1] , "*" , array[num2] , "=" , num_result, "です。")

