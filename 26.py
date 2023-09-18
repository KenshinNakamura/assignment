#26 switch-case
#整数値を入力させ、その値が1ならone、2ならtwo、3ならthree、それ以外ならothersと表示するプログラムを
#swicth-case文を使って作成せよ。

    # 整数値を入力させる
int_num = int(input("整数値を入力してください: "))
    
    # 条件をチェックして結果を表示
if int_num == 1:
    print("one")
elif int_num == 2:
    print("two")

elif int_num == 3:
    print("three")

else:
    print("other")
