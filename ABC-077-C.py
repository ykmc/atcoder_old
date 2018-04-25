import bisect
N = int(input())
A = sorted(list(map(int,input().split())))
B = sorted(list(map(int,input().split())))
C = sorted(list(map(int,input().split())))
Ans = 0
for b in B:
    Ans += bisect.bisect_left(A,b) * (N - bisect.bisect_right(C,b))
print(Ans)