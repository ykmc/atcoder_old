S = input()
K = int(input())
uniqueS = []
for s in S:
    if s not in uniqueS:
        uniqueS.append(s)
lenS = len(S)
ansS = []
uniqueS.sort()
for us in uniqueS:
    for i in range(lenS):
        for j in range(1,min(lenS-i+1,6)):
            if S[i] == us:
                if S[i:i+j] not in ansS:
                    ansS.append(S[i:i+j])
    if len(ansS) >= 5:
        break
ansS.sort()
print(ansS[K-1])