N = int(input())
C,S,F = [0]*N,[0]*N,[0]*N
for i in range(N-1):
    C[i],S[i],F[i] = map(int,input().split())
for i in range(N-1):
    T = S[i]
    for j in range(i,N-1):
        if T <= S[j]:
            T = S[j]+C[j]
        elif T%F[j] == 0:
            T += C[j]
        else:
            T += F[j] - (T%F[j]) + C[j]
    print(T)
print(0)