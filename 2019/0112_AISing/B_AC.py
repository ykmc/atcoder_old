N = int(input())
A,B = map(int,input().split())
P = list(map(int,input().split()))

ans1,ans2,ans3 = 0,0,0
for i in range(N):
    if P[i]<=A:
        ans1 += 1
    elif P[i]<=B:
        ans2 += 1
    else:
        ans3 += 1

print(min(ans1,ans2,ans3))
