#44 通貨換算
#換算したい金額（円単位）と1ドル何円かを整数値で入力すると、入力した金額が何ドル何セントか計算して表示するプログラムを作成せよ。
#1セントは1/100ドルである。結果は整数値でよい（1セント未満の端数切り捨て）。

# 金額（円単位）と1ドル何円かを整数値で入力
amount_in_yen = int(input("金額（円単位）を入力してください: "))
print(f"何円?" , amount_in_yen)

exchange_rate = int(input("1ドル何円かを入力してください: "))
print(f"1ドルは何円?" , exchange_rate)

# ドルとセントに変換
dollars = amount_in_yen // exchange_rate
cents = (amount_in_yen % exchange_rate) * 100 // exchange_rate

# 結果
print(f"{amount_in_yen}円は{dollars}ドル{cents}セント")
