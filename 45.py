#45 タクシー料金
#初乗り料金が1700mまで610円、それ以降は313mごとに80円のタクシーがある。
#このタクシーに乗った距離をm単位で入力し、料金を計算するプログラムを作成せよ。

# 乗車した距離（m単位）を入力
distance = int(input("乗車した距離（m単位）を入力してください: "))

# 初乗り料金と追加料金の計算
initial_fare = 610  # 初乗り料金（610円）
additional_fare_per_313m = 80  # 313mごとの追加料金（80円）

if distance <= 1700:
    total_fare = initial_fare
else:
    additional_distance = distance - 1700
    additional_fare = (additional_distance // 313) * additional_fare_per_313m
    total_fare = initial_fare + additional_fare

# 料金を表示
print(f"料金は{total_fare}円です。")

