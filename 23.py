#23 -5以上10未満
#整数値を入力させ、その値が-5以上10未満であればOK、そうでなければNGと表示するプログラムを作成せよ。

    # 整数値を入力させる
num = int(input("整数値を入力してください: "))
print(f"input number :" , num)

    # 条件をチェックして結果を表示
if -5 <= num < 10:
    print("OK")
else:
    print("NG")
