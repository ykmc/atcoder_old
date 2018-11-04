S = input()
lenS = len(S)
while True:
    S = S[0:lenS-2]
    lenS = len(S)
    l = lenS//2
    if S[0:l] == S[l:lenS]:
        break
print(lenS)