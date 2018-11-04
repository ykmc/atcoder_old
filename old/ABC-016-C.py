N,M = map(int,input().split())
R = [set() for i in range(N)] 
for i in range(M):
    A,B = map(int,input().split())
    R[A-1].add(B-1)
    R[B-1].add(A-1)

for i in range(N):
    Ans = set()
    for j in R[i]:
        for k in R[j]:
            if k != i and k not in R[i]:
                Ans.add(k)
    print(len(Ans))