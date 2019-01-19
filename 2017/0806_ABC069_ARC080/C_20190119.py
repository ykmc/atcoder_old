N = int(input())
A = list(map(int,input().split()))

cnt4,cnt2,cnt0 = 0,0,0 
for i in range(N):
    if A[i]%4==0:
        cnt4 += 1
    elif A[i]%2==0:
        cnt2 += 1
    else:
        cnt0 += 1

if cnt2>0:
    print("Yes" if cnt4 >= cnt0 else "No")
else:
    print("Yes" if cnt4 >= cnt0-1 else "No")