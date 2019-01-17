K = int(input())

if K==0:
    print(2)
    print(0,0)
else:
    Ans = []
    N = K%50
    M = (K-1)//50
    if K%50==0:
        N = 50
    for i in range(N):
        Ans.append(50-i + M)
    for i in range(50-N):
        Ans.append(50-N-1 + M)
    
    print(50)
    print(" ".join(map(str,Ans)))
