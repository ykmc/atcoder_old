N,T = map(int,input().split())
A = list(map(int,input().split()))

minA = A[0]
profit = 0
cnt = 0
for i in range(1,N):
    # A[i] で min(A[0..i-1])を売る場合の利益
    p = A[i]-minA
    if p==profit:
        cnt += 1 
    elif p>profit:
        profit = p
        cnt = 1
    # min(A[0..i]) の更新
    minA = min(minA,A[i])
    
print(cnt)
