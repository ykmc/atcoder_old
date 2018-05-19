N,K = map(int,input().split())
R = sorted(list(map(int,input().split())))
rating = 0
for i in range(K):
    rating = (rating+R[N-K+i])/2
print(rating)
