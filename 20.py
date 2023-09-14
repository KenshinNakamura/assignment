#20 割って掛ける
#整数値を2つ入力させ、1つめの値を2つめの値で割った結果を表示し、続けてその結果に2つめの値を掛けた結果を表示するプログラムを作成せよ。
#計算はすべて整数型で行うこと（割り切れない場合は自動的に小数点以下が切り捨てられる）。

stringX = int(input("一つ目の整数値を入力してください:"))
stringY = int(input("二つ目の整数値を入力してください:"))
result = (stringX // stringY)
result2 = (result * stringY)
print(result)
print(result2)
