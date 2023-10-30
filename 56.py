#No.56 2進数変換
#0〜65535の整数値を入力させ、
#入力値を16桁の2進数に変換して表示するプログラムを作成せよ。

#入力値
int_input_num = int(input("自然数を入力してください: "))
print (f"input number: {int_input_num}")

#2進数への変換 例10 → 1010
bin_input_num     = bin(int_input_num) #10進数の入力値を2進数に変換している
str_bin_input_num = str(bin_input_num) #数値型を文字列型に変換させている
str_bin_input_num = str_bin_input_num[2:] #変数名[2:]で先頭2文字を削除している [:2]の場合は後ろに文字を削除
##print(f"str_bin_input_num: {str_bin_input_num}") #一旦0bが消えたかの確認 後で消す

#合計16桁になるように0の追加 例.10 → 0000000000001010
 #str_bin_input_num に0を追加する 
 #16 - str_bin_input_num の結果の数だけ0を追加する この場合は12個追加する
 #12回ループさせる 回数がわかっているためforの方が良い 仮の変数[0]に一回ループするごとに1ずつ数を足していく

int_material_num     = 16 #二進数の数と比較するための数値
int_len_input_num    = len(str_bin_input_num) #str_bin_input_numの数を測る
##print(f"str_bin_input_numの数値幅{int_len_input_num}") 

##print(type(int_material_num)) #int_material_numの型を表示させる
int_bin_input_num    = int(str_bin_input_num) #int型の変数をstr型にしたい
int_result_input_num = int_material_num - int_len_input_num #桁数16 - 二進数の数を変数に入れる
##print("int_result_input_num",int_result_input_num) #上記の計算結果合計16に足りない分の数値幅

for i in range(int_result_input_num): 
    str_bin_input_num = "0" + str_bin_input_num
    ##print(str_bin_input_num) #ループチェック


#結果の出力 例. 0000000000001010

print(str_bin_input_num)


#result = bin(int_input_num)
#print (f"{result}") #←は0bがつく表示の仕方
#print (f"{int_input_num:b}") #0bなし
#print (f"{int_input_num - 1:b}")