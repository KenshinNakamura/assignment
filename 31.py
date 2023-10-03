#31 棒グラフ改
#整数値を入力させ、その個数だけ*を、5個おきに空白（スペース）を入れて表示するプログラムを作成せよ。
#入力値が0以下の値の場合は何も書かなくてよい。


num = int(input("整数値を入力してください: "))
print(f"input number :" , num)

if num <= 0:
    print("再入力")
else:
    
    for i in range(1, num + 1):
        if i % 5 == 0:
            print(" ", end="")
        else:
            print("*", end="")
    
    print()



