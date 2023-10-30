#450 foobar
#1から100までの値を繰り返しで表示するが、3の倍数の時はfoo、5の倍数の時はbarと数字の代わりに表示するプログラムを作成せよ。
#なお、3と5の両方の倍数の時はfoobarと表示される。


str1 = 0

#no.32からの引用
#↓のループで何の段まで掛けるか
for i1 in range(0, 101):
    if i1 < 101 :
       str1  += 1

       if i1 % 3 == 0 and i1 % 5 == 0:
           print("foober")
       elif i1 % 3 == 0 :
           print("foo")
       elif i1 % 5 == 0:
           print("bar")
    
       else:
           print(i1)
         

