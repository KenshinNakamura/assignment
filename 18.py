#18 配列を入力値で初期化
#要素数10の整数型の配列を宣言し、整数値を入力させ、すべての配列の要素を入力値として、すべての要素の値を表示するプログラムを作成せよ。
#
# 整数型のリストを宣言し、各要素を初期化
array = [0] * 10

# リストの要素を順に表示
user_input = int(input(f"整数値を入力してください :"))
print(f"input number :" , user_input)
for i in range(10):
    
    array[i]   = user_input

for i in range(10):
    print(array[i]) 


#(1) 入力した値を配列10個に格納
#(2) 配列10個を表示