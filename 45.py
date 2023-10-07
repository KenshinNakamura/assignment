#45 タクシー料金
#初乗り料金が1700mまで610円、それ以降は313mごとに80円のタクシーがある。
#このタクシーに乗った距離をm単位で入力し、料金を計算するプログラムを作成せよ。

# 乗車した距離（m単位）を入力
NUM = int(input("乗車した距離（m単位）を入力してください: "))
print(f"距離 {NUM}")

# 初乗り料金と追加料金の計算
Price_1= 610  # 初乗り料金（610円）
Price_2 = 80  # 313mごとの追加料金（80円）

if  NUM<= 1700:
    Result = Price_1
else:
    distance1 = NUM - 1700
    
    # 料金単位で割った回数（切り上げ）
    count = (distance1 + 312) // 313
    
    # 計算
    Add_Price = count * Price_2
    
    # 合計料金の計算
    Result = Price_1 + Add_Price

#出力
print(f"金額{Result}")

