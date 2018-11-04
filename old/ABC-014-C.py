N = int(input())
A = [0]*1000002
for i in range(N):
    a,b = map(int,input().split())
    A[a] += 1
    A[b+1] -= 1
S = [0]*1000002
S[0] = A[0]
for i in range(1000001):
    S[i+1] = S[i]+A[i+1]
print(max(S))