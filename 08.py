#08 正の整数?
#整数値を入力させ、値が正であればpositiveと表示するプログラムを作成せよ。
#ただし0は正には含まない。
string = int(input("一つ目の整数値を入力してください:"))
if string > 0:
    print("positive")
    
elif string == 0:
    print("zero")

else :
    print("negative number")

print(f"input number :" , string)

string2 = int(input("二つ目の整数値を入力してください:"))
if string2 > 0:
    print("positive")

elif string == 0:
    print("zero")

else :
    print("negative number")

print(f"input number :" , string2)