N = int(input())
S = input()

left,right = [0]*N,[0]*N
cnt = 0
for i in range(1,N):
    if S[i-1]=="W":
        cnt += 1
    left[i] = cnt
cnt = 0
for i in range(N-2,-1,-1):
    if S[i+1]=="E":
        cnt += 1
    right[i] = cnt

ans = 10**9
for i in range(N):
    ans = min(ans, left[i]+right[i])

print(ans)