#16 0でおしまい
#整数値を入力させ、入力値が0でなければ再度入力させ、0であれば終了するプログラムを作成せよ。

while True:
    # 整数値の入力を受け付ける
    number = int(input("整数値を入力してください（0で終了）: "))
    print(f"input number :" , number)

    # 入力値が0でない場合、再度入力を促す
    if number != 0:
        continue
        
    else:
        # 入力値が0の場合、プログラムを終了
        print("プログラムを終了します。")
        break

