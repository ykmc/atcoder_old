N = int(input())
P = []
for i in range(N):
    P.append(input())

Ans = []
for i in range(N):
    ans = 0
    p = P[i][::-1]
    while p[0]=="0":
        p = p[1::]
        ans += 1
    Ans.append(ans) 

print(min(Ans))