#No. 54 最大最小
#まずデータの個数を入力させ、次にデータの個数だけ整数値を入力させる。この入力データの中で最大値と最小値を求め表示するプログラムを作成せよ。
#データの個数は100個までとする。なお、データの個数とデータはファイルからリダイレクトで入力させればよいので、入力のためのメッセージは不要である（実行例を参照すること）。

#作成途中
import csv

My_num = []

MyPath = '/Users/nakamurakenshin/Documents/課題/基礎編/data.csv'

with open(MyPath) as f:
    
    data = csv.reader(f)
    
    for i in data:
        print(i)
        for j in i:
            My_num.append(int(j))
    print(My_num)
    print(max(My_num))
    print(min(My_num))

#import csv
#with open("data.csv") as f:
#    for row in csv.reader(f, quoting=csv.QUOTE_NONNUMERIC):
#        print(f"Row: {row}")
#上記のコードの欠点 float型の為、小数点がついた状態で表示させてしまう
#int は整数型
#csv.reader 配列