#No.56 2進数変換
#0〜65535の整数値を入力させ、
#入力値を16桁の2進数に変換して表示するプログラムを作成せよ。

num1 = int(input("自然数を入力してください: "))
print(f"input number: {num1}")

print (bin(num1)) #←は0bがつく表示の仕方
#print (f"{num1:b}") #0bなし
