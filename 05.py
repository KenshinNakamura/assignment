#05 四則演算
#整数値を2つ入力させ、それらの値の和、差、積、商と余りを求めるプログラムを作成せよ。
#なお、差と商は1つ目の値から2つ目の値を引いた、あるいは割った結果とする。
#余りは無い場合も0と表示するのでよい。
string1 = int(input("整数値を入力してください:"))
string2 = int(input("二つ目の整数値を入力してください:"))
#input  = 123
#input2 = 7
result1 = ("和:" + string1 + string2)
result2 = ("差:" + string1 - string2)
result3 = ("積:" + string1 * string2)
result4 = ("商:" + string1 // string2)
result5 = ("余り:" + string1 % string2)

print(result1)
print(result2)
print(result3)
print(result4)
print(result5)

string3 = int(input("三つ目の整数値を入力してください:"))
string4 = int(input("四つめの整数値を入力してください:"))
#input3 =123
#input4 =3
result6  =(string3 + string4)
result7  =(string3 - string4)
result8  =(string3 * string4)
result9  =(string3 // string4)
result10 =(string3 % string4)

print("和:" + result6)
print("差:" + result7)
print("積:" + result8)
print("商:" + result9)
print("余り:" + result10)