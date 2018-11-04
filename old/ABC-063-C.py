N = int(input())
S = [int(input()) for _ in range(N)]
sumS = sum(S)
T = list(filter(lambda x : x%10!=0, S))
T.sort()
if len(T)==0:
    print(0)
else:
    for t in T:
        if sumS%10!=0:
            break
        else:
            sumS -= t
    print(sumS)