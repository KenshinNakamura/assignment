#05 四則演算
#整数値を2つ入力させ、それらの値の和、差、積、商と余りを求めるプログラムを作成せよ。
#なお、差と商は1つ目の値から2つ目の値を引いた、あるいは割った結果とする。
#余りは無い場合も0と表示するのでよい。
string1 = int(input("一つ目の整数値を入力してください:"))
string2 = int(input("二つ目の整数値を入力してください:"))
#input  = 123
#input2 = 7
print(f"input 1st number :" ,string1)
print(f"input 2nd number :" ,string2)
result1 = (string1 + string2)
result2 = (string1 - string2)
result3 = (string1 * string2)
result4 = (string1 // string2)
result5 = (string1 % string2)

print(f"和:" ,result1)
print(f"差:" , result2)
print(f"積:" ,result3)
print(f"商:" ,result4 , "," , f"余り:" ,result5) 

string3 = int(input("三つ目の整数値を入力してください:"))
string4 = int(input("四つめの整数値を入力してください:"))
#input3 =123
#input4 =3
print(f"input 1st number :" ,string3)
print(f"input 1st number :" ,string4)
result6  = (string3 + string4)
result7  = (string3 - string4)
result8  = (string3 * string4)
result9  = (string3 // string4)
result10 = (string3 % string4)

print("和:" , result6)
print("差:" , result7)
print("積:" , result8)
print("商:" , result9 , "," , "余り:" , result10) 