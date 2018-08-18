S = input()
K = int(input())

S2 = ""
for i in range(len(S)):
    if S[i]=="1":
        S2 += "1"
    else:
        S2 += S[i]*101
        break

if K<100:
    print(S2[K-1])
else:
    print(S2[100])
