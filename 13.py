#13 カウントアップ
#整数値を入力させ、0から入力値まで数を1ずつ増やして表示するプログラムを作成せよ。
#try:
 #   string = int(input("整数値を入力してください:"))
#y = 0

#for string in range(y +1):
        #print(y)

try:
    # 整数値の入力を受け付ける
    n = int(input("整数値を入力してください: "))

    # 0から入力値までの数を1ずつ増やして表示
    for i in range(n +1):
        print(i)
except ValueError:
    print("無効な入力です。整数値を入力してください。")
