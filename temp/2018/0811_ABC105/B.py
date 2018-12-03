N = int(input())

Ans = "No"
for i in range(20):
    for j in range(30):
        if i*7 + j*4 == N:
            Ans = "Yes"

print(Ans)
