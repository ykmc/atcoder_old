A,B,K = map(int,input().split())
Ans = []
for i in range(1,101):
    if A%i==0 and B%i==0:
        Ans.append(i)

Ans.sort(reverse=True)
print(Ans[K-1])