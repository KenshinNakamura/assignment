#09 正? 負? 0?
#整数値を入力させ、値が正であればpositive、
#負であればnegative、0であればzeroと表示するプログラムを作成せよ。
string = int(input("一つ目の整数値を入力してください:"))
if string > 0:
    print("positive")
    
elif string == 0:
    print("zero")

else :
    print("negative")

print(f"input number :" , string)

string2 = int(input("二つ目の整数値を入力してください:"))
if string2 > 0:
    print("zero")

elif string == 0:
    print("zero")

else :
    print("not zero")

print(f"input number :" , string2)