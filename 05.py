#05 四則演算
#整数値を2つ入力させ、それらの値の和、差、積、商と余りを求めるプログラムを作成せよ。
#なお、差と商は1つ目の値から2つ目の値を引いた、あるいは割った結果とする。
#余りは無い場合も0と表示するのでよい。
string1 = int(input("整数値を入力してください:"))
string2 = int(input("二つ目の整数値を入力してください:"))
#input  = 123
#input2 = 7
print(string1 + string2)
print(string1 - string2)
print(string1 * string2)
print(string1 // string2)
print(string1 % string2)

string3 = int(input("三つ目の整数値を入力してください:"))
string4 = int(input("四つめの整数値を入力してください:"))
#input3 =123
#input4 =3
print(string3 + string4)
print(string3 - string4)
print(string3 * string4)
print(string3 // string4)
print(string3 % string4)