#No.57 テスト集計
#まず受験者数を入力させ、次に受験者数ごとに英語、数学、国語の点数をスペースで区切って入力させる（具体的な入力方法は下記のscanfの使い方の説明、および入力データの中身を見よ）。
#入力が終了したら、英語、数学、国語の平均点、および各受験生の合計点を計算して表示するプログラムを作成せよ。
#受験者数は100人までとする。なお、データの個数とデータはファイルからリダイレクトで入力させればよいので、入力のためのメッセージは不要である（実行例を参照すること）。

#no.54で似た事例を行ったのでそれを参考に作成しています
#受験者数はdata.csvの一番上の数字 その下の行に英 数 国とある

#データファイルの読み込み
#scanfの代理工程
#データは英,数,国の順でならんんでいる
import csv #csvの読み込み
MyPath_data = '/Users/nakamurakenshin/Documents/課題/基礎編/data_57.csv' #data57.csvのデータを読み込みMyPathにしまっている


loop_count       = 0

Total_English_score  = 0
Total_Math_score     = 0
Total_Language_score = 0

int_sum_score = 0


with open(MyPath_data) as My_Path_data_f: #MyPath_dataを開きMyPath_data_fにしまっている

    array_all_data            = csv.reader(My_Path_data_f) #一行目の読み込み
    
    
    #英語の平均点
    for i in array_all_data:                 #データ全体を変数iに入れてループさせている
        int_English_score     = int(i[0])     #i はstr型だったのでint型に変換し変数int_English_scoreに入れている
        int_Math_score        = int(i[1])
        int_Language_score    = int(i[2])
        loop_count           += 1                 #ループするたびにloop_countに1を足していきループした回数を可視化させる
        Total_English_score  += int_English_score 
                                        #↑は変数Total_English_scoreに英語の点数を全て足して変数に入れている 合計値は463
        Total_Math_score     += int_Math_score
        Total_Language_score += int_Language_score

    My_Path_data_f.seek(0)
    Result_English_score      = Total_English_score // loop_count
    Result_Math_score         = Total_Math_score // loop_count
    Result_Language_score     = Total_Language_score // loop_count
    print(f"英語の平均点 {Result_English_score}")
    print(f"数学の平均点 {Result_Math_score}")
    print(f"国語の平均点 {Result_Language_score}")

        #print(type(int_English_score)) #int_English_scoreの文字タイプを調べる
        #print(i)                       #全体のデータを一人ずつ調べる
        #print(loop_count)              #何回ループしたのかを調べる
        #print(Total_English_score)     #英語の合計点を調べる 正しい数値は463

    

    #各受験生の合計点
    #forでEng,math,Lan をループ毎に足してループ毎にprintさせる
    #ループは2個で

    loop_count = 0

    for i_sum in array_all_data:
        int_English_score     = int(i_sum[0])
        int_Math_score        = int(i_sum[1])
        int_Language_score    = int(i_sum[2])
        loop_count   += 1

        #print(int_English_score,int_Math_score,int_Language_score)
        int_sum_score = int_English_score + int_Math_score + int_Language_score
        print(f"生徒{loop_count}の合計点 {int_sum_score}")
