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

# 数値の入力

# ループ：0以上の整数値が入力されるまで、ループから出ることができない

int_input_num_1 = int(input("0より大きい数値を入力してください (一つ目):"))
int_input_num_2 = int(input("0より大きい数値を入力してください (二つ目):"))
int_input_num_3 = int(input("0より大きい数値を入力してください (三つ目)"))
int_input_num_4 = int(input("0より大きい数値を入力してください (四つ目):"))
int_input_num_5 = int(input("0より大きい数値を入力してください (五つ目):"))

while int_input_num_1 < 0 or int_input_num_2 < 0 or int_input_num_3 < 0 or int_input_num_4 < 0 or int_input_num_5 < 0 :
    print()
    int_input_num_1 = int(input("再入力してください (一つ目):"))
    int_input_num_2 = int(input("再入力してください (二つ目):"))
    int_input_num_3 = int(input("再入力してください (三つ目)"))
    int_input_num_4 = int(input("再入力してください (四つ目):"))
    int_input_num_5 = int(input("再入力してください (五つ目):"))

print()
print(f"{int_input_num_1}[1]")
print(f"{int_input_num_2}[1]")
print(f"{int_input_num_3}[1]")
print(f"{int_input_num_4}[1]")
print(f"{int_input_num_5}[1]")

# 改行
print("")

# 本処理

    #print(f"{int_input_num_5}[5]")
result = [int_input_num_1, int_input_num_2, int_input_num_3, int_input_num_4, int_input_num_5]

    # 数値が入力された5個、5回分のループ
for i in result:
        # 初期化
    int_graph_1 = ""    # 変数名、わかりにくすぎ
        #print(f"i Loop Start")
        # 数値の数だけループさせる（1だったら1回、10だったら10回ループ）
    for j in range(1,i + 1):

        if j % 5 == 0:
                # 5で割り切れたら、「* 」を入れる
            int_graph_1 += "* "

        else:
                # 5で割り切れない場合、「*」を入れる
            int_graph_1 += "*"

    print(j, ":" ,int_graph_1)