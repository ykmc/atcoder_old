A,B,Q = map(int,input().split())
S = [-float("inf")]+[int(input()) for _ in range(A)]+[float("inf")]
T = [-float("inf")]+[int(input()) for _ in range(B)]+[float("inf")]
X = [int(input()) for _ in range(Q)]

from bisect import bisect_left

for x in X:
    Si,Ti = bisect_left(S,x),bisect_left(T,x)
    Sw,Se = abs(x-S[Si-1]),abs(x-S[Si])
    Tw,Te = abs(x-T[Ti-1]),abs(x-T[Ti])
    print(min(max(Sw,Tw),max(Se,Te),2*min(Sw,Te)+max(Sw,Te),2*min(Tw,Se)+max(Tw,Se)))