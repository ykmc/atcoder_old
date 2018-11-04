A,B,C,K = map(int,input().split())
Ans = 0
if K%2==1:
    Ans = B-A
else:
    Ans = A-B
print(Ans if Ans <= 10**18 else "Unfair")