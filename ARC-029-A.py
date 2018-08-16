N = int(input())
T = []
for i in range(N):
    T.append(int(input()))

Ans = 10000
for i in range(2**N):
    bits = bin(2**N+i)[3:]
    a,b = [],[]
    for j in range(N):
        if bits[j]=="0":
            a.append(T[j])
        else:
            b.append(T[j])
    Ans = min(Ans,max(sum(a),sum(b)))

print(Ans)