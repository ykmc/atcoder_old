N,K = map(int,input().split())
D = set(input().split())

for i in range(N,100000):
    # 禁止文字との共通集合がなければ良い
    if not D & set(str(i)):
        break

print(i)