S = input()

N = len(S)
a,z = 0,0
for i in range(N):
    if S[i]=="A":
        a = i
        break
for i in range(N):
    if S[N-1-i]=="Z":
        z = N-1-i
        break

print(z-a+1)