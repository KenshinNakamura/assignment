#48 繰り返し計算
#最初に2以上の整数値を入力し、次の規則で計算し、計算回数と計算結果を表示し、
#計算結果が1になるまで繰り返すプログラムを作成せよ。
#規則：ある値が偶数ならその値を1/2にする。奇数ならその値を3倍して1を足す。

num = int(input("整数値を入力してください: "))
if num >= 2:
    print(f"input number :" , num)

else:
    print(f"再入力してください")

count = 0

#for count in range(1, {count} + 1):

#whileで条件指定 n
while num > 1:
    
    #if num == 1:
        
    #↓偶数の場合
    if num % 2 == 0:
        num = num // 2
     #奇数の場合
    else:
        num = (num * 3) + 1
    
    count += 1
    print(f"{count} : {num}")
    if num == 1:
        break