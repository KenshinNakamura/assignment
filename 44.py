#44 通貨換算
#換算したい金額（円単位）と1ドル何円かを整数値で入力すると、入力した金額が何ドル何セントか計算して表示するプログラムを作成せよ。
#1セントは1/100ドルである。結果は整数値でよい（1セント未満の端数切り捨て）。

# 金額（円単位）と1ドル何円かを整数値で入力
num1 = int(input("求める金額(円)を入力してください: "))
num2 = int(input("現在の1ドルの値段(円)を入力してください: "))

#セントでは余りを求める
yen = num1
dole_yen = num2
dole_result = yen // dole_yen
cent_result = yen % dole_yen 

#出力
print(f"{yen}円は{dole_result}ドル{cent_result}セント")
