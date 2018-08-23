from collections import Counter
N = int(input())
T = []
for i in range(N):
    T.append(int(input()))

C = Counter(T).most_common()
C.sort()

mod = 10**9+7
t = 0
Ans1,Ans2 = 0,1
for c in C:
    key,val = c
    for i in range(val):
        t += key
        Ans1 += t
        Ans2 = (Ans2*(val-i))%mod

print(Ans1)
print(Ans2)