N = int(input())

# Nの桁数
lenN = len(str(N))

Ans = 0
for i in range(lenN):
    d = 10**(i+1)
    q = N//d
    r = N%d
    # ループ分
    Ans += (10**i)*q
    # 余り分
    if r >= 2*(10**i):
        Ans += 10**i
    elif r >= (10**i):
        Ans += r-10**i+1

print(Ans)