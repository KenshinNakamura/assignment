#38 さらに・配列要素の参照
#{3, 7, 0, 8, 4, 1, 9, 6, 5, 2}で初期化される大きさ10の整数型配列を宣言し、
#最初は参照する要素番号を0とし、この参照する要素番号の配列要素の値を表示し、
#次にその配列要素の値を次の参照する要素番号とし、この次の参照する要素番号の配列要素の値を表示し、
#さらにその配列要素の値を次の参照する要素番号とし、……を10回繰り返すプログラムを作成せよ。
#（具体的にどのような手順かは実行例を見て考えよう。）

#num1 = int(input("整数値を入力してください: "))
#num2 = int(input("整数値を入力してください: "))

# 配列を初期化
array = [3, 7, 0, 8, 4, 1, 9, 6, 5, 2]

index_num = 0

for _ in array:
    print(f"{index_num}番目の要素: {array[index_num]}" )

    index_num = array[index_num]
