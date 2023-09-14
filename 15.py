#15 2ずつカウントアップ
#整数値を入力させ、0から入力値を超えない値まで2ずつ増やして表示するプログラムを作成せよ。
stringX = int(input("整数値を入力してください:"))
stringY = int(input("整数値を入力してください:"))


while stringX<stringY:
  print(stringX)  
  stringX+= 2