N = int(input())
S = input()

L,maxL = 0,0
Ans = 0
for i in range(N):
    if S[i]=="-":
        maxL = max(maxL,L)
        L = 0
        Ans += 1
    else:
        L += 1
        Ans += 1/(L+1)

print(Ans -1 +1/(maxL+2))
