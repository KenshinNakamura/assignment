#58 棒グラフ
#0以上の整数値を5つ入力させ、それぞれの値に対して、次の形式でグラフを描くプログラムを作成せよ。
#形式：左端に値を表示し、適切に空白を空けて":"を書く（:で揃えるためにタブ\tを使うとよい）。その後ろに値の数だけ*を描くが、5個おきに空白を１つ入れる。具体例は下記の実行例を参照すること。
int_graph_1 = ""
int_graph_2 = ""
int_graph_3 = ""
int_graph_4 = ""
int_graph_5 = ""
int_num     = 0

# 初期化
int_input_num_1 = -1
int_input_num_2 = -1

# ループの参考
'''
while int_input_num_1 >= 0:
    print(f"0以上の整数値を入力して下さい")

# print(f"OK")
'''

# 数値の入力

# ループ：0以上の整数値が入力されるまで、ループから出ることができない

int_input_num_1 = int(input("0より大きい数値を入力してください (一つ目):"))
while int_input_num_1 < 0: #int_input_num_1が0より小さい場合ループする　抜ける場合は control + c
    int_input_num_1 = int(input("2個め:")) 
    print(f"{int_input_num_1}[1]")

int_input_num_2 = int(input("0より大きい数値を入力してください (二つ目):"))
while int_input_num_2 < 0:
    int_input_num_2 = int(input("2個め"))
    print(f"{int_input_num_2}[1]")

int_input_num_3 = int(input("0より大きい数値を入力してください (三つ目)"))
while int_input_num_3 < 0:
    int_input_num_3 = int(input("3個め"))
    print(f"{int_input_num_3}[1]")

int_input_num_4 = int(input("0より大きい数値を入力してください (四つ目):"))
while int_input_num_4 < 0:
    int_input_num_4 = int(input("4個め"))
    print(f"{int_input_num_4}[1]")

int_input_num_5 = int(input("0より大きい数値を入力してください (五つ目):"))
while int_input_num_5 < 0:
    int_input_num_5 = int(input("5個目"))
    print(f"{int_input_num_5}[1]")

# 改行
print("")

# 本処理
if isinstance(int_input_num_5, (int)):
    #print(f"{int_input_num_5}[5]")
    result = [int_input_num_1, int_input_num_2, int_input_num_3, int_input_num_4, int_input_num_5]

    # 数値が入力された5個、5回分のループ
    for i in result:
        # 初期化
        int_graph_1 = ""    # 変数名、わかりにくすぎ
        #print(f"i Loop Start")
        # 数値の数だけループさせる（1だったら1回、10だったら10回ループ）
        for j in range(1,i + 1):
            #print(f"j Loop Start")
            #print(j)
            if j % 5 == 0:
                # 5で割り切れたら、「* 」を入れる
                int_graph_1 += "* "
                #int_num += 1
                #print()
                    #print("回数",int_num)
            else:
                # 5で割り切れない場合、「*」を入れる
                int_graph_1 += "*"
                #int_num += 1
                #print("回数",int_num)
            #print(f"int_graph_1={int_graph_1}")
            #print("")
        #print(int_input_num_1, ":" ,int_graph_1)
        print(j, ":" ,int_graph_1)
        #print("j" ,j)
else:
    print(f"再入力してください")    # おかしい

#print(int_input_num_1, ":" ,int_graph_1)
#print("i :" ,i)
#print(result)

#isinstance 