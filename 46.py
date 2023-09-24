#46 入場料
#神山美術館の入場料金は、一人600円であるが、5人以上のグループなら一人550円、20人以上の団体なら一人500円である。
#人数を入力し、入場料の合計を計算するプログラムを作成せよ。

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

