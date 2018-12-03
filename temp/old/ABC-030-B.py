N,M = map(int,input().split())

N %= 12
deg = abs(N*30+M*0.5 - M*6)
print(min(deg,360-deg))