#46 入場料
#神山美術館の入場料金は、一人600円であるが、5人以上のグループなら一人550円、20人以上の団体なら一人500円である。
#人数を入力し、入場料の合計を計算するプログラムを作成せよ。

#入場者数
num1 = int(input("入場者数を入力してください: "))
print(f"入場者数" , num1)

if 5 > num1 >= 1:
    ticket = 600

elif num1 >= 5:
    ticket = 550

elif num1 >= 20:
    ticket = 500

else:
    num1 = 600

result = num1 * ticket

# 料金を表示
print(f"{num1}人の時の入場料金は、一人{ticket}円の場合、合計{result}円です。")

