#22 -10以下または10以上
#整数値を入力させ、その値が-10以下、または、10以上であればOKと表示するプログラムを作成せよ。

    # 整数値を入力させる
int_num = int(input("整数値を入力してください: "))
print(f"input number :" , int_num)

    # 条件をチェックして結果を表示
if int_num <= -10 or int_num >= 10:
    print("OK")
else:
    print("条件を満たしません。")
