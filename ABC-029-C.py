N = int(input())

C = ["a","b","c"]
Ans = ["a","b","c"]

for _ in range(N-1):
    tmp = []
    for c in C:
        for ans in Ans:
            tmp.append(c+ans)
    Ans = tmp

for ans in Ans:
    print(ans)



