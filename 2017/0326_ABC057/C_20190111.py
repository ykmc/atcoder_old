N = int(input())

ans = 10**10
for i in range(1,int(N**.5)+1):
    if N%i==0:
        ans = min(ans,max(len(str(i)),len(str(N//i))))

print(ans)