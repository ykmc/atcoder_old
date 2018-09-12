# [AtCoder Beginner Contest 105](https://beta.atcoder.jp/contests/abc105/tasks)

|   | Task Name | Score |
|:---:|:---|---:|
| A | AtCoder Crackers | 100 |
| B | Cakes and Donuts | 200 |
| C | Base -2 Number | 300 |
| D | Candy Distribution | 400 |

## A.AtCoder Crackers
全員に1枚ずつ配っていけば、最も多くもらった人と最も少なくもらった人の差は1以内となる。
0になるのはNがKで割り切れる時。

## B.Cakes and Donuts
全探索。
ケーキの個数x, ドーナツの個数yとして、4x + 7y = N となる(x,y)の組を数える。

## C.Base -2 Number
10進数をn進数に変換するのと同じ計算方法で、n = -2 とする。
余りの扱いにやや注意。

## D.Candy Distribution
部分和が M の倍数であれば良い。言い換えると、部分和を M で割った余りが 0 であれば良い。
部分和は、元の数列の累積和の差を用いて高速に計算可能。
つまり、累積和を M で割った余りが同じものの組み合わせの総数が求める答えとなる。

