S = input()
N = len(S)

Ans = [-1,-1]
# 1-indexedであることに注意。。。
for i in range(N-1):
    if S[i]==S[i+1]:
        Ans = [i+1,i+2]
        break
for i in range(N-2):
    if S[i]==S[i+2] and S[i]!=S[i+1]:
        Ans = [i+1,i+3]
        break

print(Ans[0],Ans[1])