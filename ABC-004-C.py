N = int(input())

# 周期30
N %= 30

Ans = [1,2,3,4,5,6]
for i in range(N):
    ix,iy = i%5,i%5+1
    nx,ny = Ans[ix],Ans[iy]
    Ans[ix],Ans[iy] = ny,nx

print("".join(map(str,Ans)))
