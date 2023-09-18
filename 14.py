#14 カウントダウン
#整数値を入力させ、入力値から0まで数を1ずつ減らして表示するプログラムを作成せよ。
int_num = int(input("整数値を入力してください:"))

while int_num > 0:
  print(int_num)  
  int_num -= 1