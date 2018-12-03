N = int(input())
S = input()

score = {"A":4,"B":3,"C":2,"D":1,"F":0}

Ans = 0
for i in range(N):
    Ans += score[S[i]]

print(Ans/N)
