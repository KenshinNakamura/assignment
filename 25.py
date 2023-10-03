#25 -10未満?、-10以上0未満?、0以上?
#整数値を入力させ、その値が-10未満ならrange 1、
#-10以上0未満であればrange 2、0以上であればrange 3、と表示するプログラムを作成せよ。

    # 整数値を入力させる
int_num = int(input("整数値を入力してください: "))
print(f"input number :" , int_num)

    # 条件をチェックして結果を表示
if int_num < -10:
    print("range 1")
elif 0 > int_num >= -10:
    print("range 2")

elif int_num >= 0:
    print("range 3")

else:
    print("NG")
