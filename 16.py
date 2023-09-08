#16 0でおしまい
#整数値を入力させ、入力値が0でなければ再度入力させ、0であれば終了するプログラムを作成せよ。
x = input(77)
numbers = x
for number in numbers:
    print(number)
    # 変数 number が 777 のとき「 777が見つかったので処理を終了します 」と出力した後、処理を終了させてください
    if number == 777:
      print("777が見つかったので処理を終了します")
      break