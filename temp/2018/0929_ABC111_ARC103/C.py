from collections import Counter
N = int(input())
V = list(map(int,input().split()))

v1 = V[0::2]
v2 = V[1::2]

c1 = Counter(v1).most_common()
c2 = Counter(v2).most_common()

# 数字が1つしかない場合に"2番目"をダミーで追加
c1.append((0,0))
c2.append((0,0))

if c1[0][0]==c2[0][0]:
    print(min(N-(c1[0][1]+c2[1][1]), N-(c1[1][1]+c2[0][1])))
else:
    print(N- (c1[0][1]+c2[0][1]))