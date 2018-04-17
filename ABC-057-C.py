N = int(input())
ans = 10**10

def F(A,B):
    return max(len(str(A)), len(str(B)))

rootN = int(N**.5)
for i in range(1,rootN+1):
    if N%i == 0:
        ans = min(ans,F(N//i,i))

print(ans)
