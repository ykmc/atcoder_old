N = int(input())
S = input()
from collections import Counter

C = Counter(S).items()

ans = 1
modulo = 10**9+7
for ck,cv in C:
    ans *= cv+1
    ans %= modulo

print(ans-1)