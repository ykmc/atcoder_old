N = int(input())
P = list(map(int,input().split()))+[0]
i,Ans = 0,0
while i<N:
    if P[i] == i+1:
        if P[i+1]==i+2:
            Ans += 1
            i += 1
        else:
            Ans += 1
    i += 1
print(Ans)
