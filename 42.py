#42 小さい順?
#整数値を3つ入力させ、それらの値が小さい順（等しくてもよい）に並んでいるか判定し、
#小さい順に並んでいる場合はOK、そうなっていない場合はNGと表示するプログラムを作成せよ。

num1 = int(input("一つ目の要素番号を入力してください: "))
num2 = int(input("二つ目の要素番号を入力してください: "))
num3 = int(input("三つ目の要素番号を入力してください: "))

print(f"input number :" , num1)
print(f"input number :" , num2)
print(f"input number :" , num3)

if num1 <= num2 <= num3:
    print("おk")

else:
    print("NG")