#48 繰り返し計算
#最初に2以上の整数値を入力し、次の規則で計算し、計算回数と計算結果を表示し、
#計算結果が1になるまで繰り返すプログラムを作成せよ。
#規則：ある値が偶数ならその値を1/2にする。奇数ならその値を3倍して1を足す。

num1 = int(input("整数値を入力してください: "))
print(f"input number :" , num1)

count = 0

for count in range(1, count + 1):
    if num1 == 1:
        break
    
    if num1 % 2 == 0:
        num1 = num1 // 2
    else:
        num1 = (num1 * 3) + 1
    count += 1
    print(f"{count} : {num1}")