#43 2次方程式の解の判別
#2次方程式 ax^2 + bx + c = 0 （x^2はxの2乗の意味）の係数a, b, cを入力し、2次方程式の解が2つの実数解か、
#重解か、2つの虚数解かを判別するプログラムを作成せよ。

import math

# 係数a, b, cを入力
a = float(input("aを入力してください: "))
b = float(input("bを入力してください: "))
c = float(input("cを入力してください: "))

print(f"input number :" , a)
print(f"input number :" , b)
print(f"input number :" , c)

# 判別式を計算
discriminant = b**2 - 4*a*c

# 判別式に基づいて解のタイプを判別
if discriminant > 0:
    print("2つの実数解があります。")
    x1 = (-b + math.sqrt(discriminant)) / (2*a)
    x2 = (-b - math.sqrt(discriminant)) / (2*a)
    print(f"x1 = {x1}, x2 = {x2}")
elif discriminant == 0:
    print("重解があります。")
    x1 = -b / (2*a)
    print(f"x1 = x2 = {x1}")
else:
    print("2つの虚数解があります。")
    real_part = -b / (2*a)
    imaginary_part = math.sqrt(-discriminant) / (2*a)
    solution1 = complex(real_part, imaginary_part)
    solution2 = complex(real_part, -imaginary_part)
    print(f"x1 = {solution1}, x2 = {solution2}")
