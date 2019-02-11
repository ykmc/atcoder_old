N = int(input())
A,B = map(int,input().split())
P = list(map(int,input().split()))

Ans = [0]*3
for i in range(N):
    if P[i]<=A:
        Ans[0] += 1
    elif P[i]<=B:
        Ans[1] += 1
    else:
        Ans[2] += 1

print(min(Ans))