## AtCoder Beginner Contest 109

### 概要

https://beta.atcoder.jp/contests/abc109

|   | Task Name      | Score |
|:-:|:---------------|------:|
| A | ABC333         |   100 |
| B | Shiritori      |   200 |
| C | Skip           |   300 |
| D | Make Them Even |   400 |

### 考察

#### A.ABC333
2数の積が奇数になるためには、どちらも奇数である必要がある。
よって与えられた2数の積が奇数かどうかで場合分けすれば良い。

#### B.Shiritori
与えられたしりとりのルールを満たすか調べれば良い。
1. 「単語の末尾の文字」と「次の単語の最初の文字」が一致している
2. 同じ単語を複数回使っていない

#### C.Skip
全ての都市の座標から初期位置 X を減算し「初期位置からその都市への移動距離」とする。
ある都市に訪れることができる場合、移動距離の単位 D は座標 x - X の約数である。
全ての都市を訪れる必要があるので、全ての都市の座標 x_n - X の公約数である。
求める答えは最大の D なので、要するに最大公約数ということになる。

#### D.Make Them Even
あるマスにコインが奇数個ある場合、

- どこかに1枚渡す
- 自分自身は以降1枚も受け取らない

を満たす場合、終了時に偶数であることを確定できる。
よって「全てのマスを順番に訪れる順路を一つ作って奇数なら次回訪れる予定のマスにコインを1枚渡す」
で解くことが可能。
結果、最後の1マス以外は全て偶数枚、最後のマスは全体の合計が偶数の時に偶数になる。


