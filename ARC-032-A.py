from math import ceil
N = int(input())

M = N*(N+1)//2

Ans = "WANWAN"
if N==1:
    Ans = "BOWWOW"
else:
    Lim = ceil(M**0.5)
    for i in range(2,Lim+1):
        if M//i == M/i:
            Ans = "BOWWOW"
            break

print(Ans)