#19 配列に入力値を格納
#要素数5の整数型の配列を宣言し、すべての配列に対して順に入力された整数値を代入し、
#すべての要素の値を表示するプログラムを作成せよ。

# 要素数5の整数型の配列を宣言
array = [0] * 5

# ユーザーからの入力で配列を初期化
for i in range(5):
    while True:
        try:
            array[i] = int(input(f"整数値を入力してください（{i+1}/5）: "))
            break  # 正しい入力があるまでループ
        except ValueError:
            print("無効な入力です。整数値を入力してください。")

# 配列の要素の値を表示
print("配列の要素の値:")
for i in range(5):
    print(f"array[{i}] = {array[i]}")

#不明点多々あり
