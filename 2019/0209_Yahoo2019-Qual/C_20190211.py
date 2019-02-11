K,A,B = map(int,input().split())

if B-A <= 2:
    print(K+1)
else:
    c = max(0,K-(A-1))//2
    print((B-A)*c + K-c*2+1)