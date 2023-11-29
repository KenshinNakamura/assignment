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
input_num_int = -1
input_num_int = -1
input_num_ints = []

j = 0

# 数値の入力

# ループ：0以上の整数値が入力されるまで、ループから出ることができない

for index in range(1,6):
    input_num_int = int(input("0より大きい数値を入力してください :"))
    while input_num_int < 0 :
        print()
        input_num_int = int(input("再入力してください :"))

    input_num_ints.append(input_num_int)

print()
print(input_num_int)
print(index)
print()
print(f"{input_num_int}")

# 改行
print("")

# 本処理

    #print(f"{input_num_int}[5]")

    # 数値が入力された5個、5回分のループ

print(input_num_ints)
for i in input_num_ints:
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