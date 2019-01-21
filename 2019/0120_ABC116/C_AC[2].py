N = int(input())
H = list(map(int,input().split()))

ans = 0
st = "0"
while H!=[0]*N:
    for i in range(N):
        if H[i]>0:
            st = "+"
            H[i] -= 1
        elif st=="+" and H[i]==0:
            st = "0"
            ans += 1
    if st=="+":
        ans += 1
    st = "0"

print(ans)



