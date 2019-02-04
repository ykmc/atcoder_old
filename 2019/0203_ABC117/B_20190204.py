N = int(input())
L = list(map(int,input().split()))
L.sort()
print("Yes" if sum(L[0:N-1]) > max(L) else "No")