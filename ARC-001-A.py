N = int(input())
S = input()

Ans = []
for i in range(4):
    Ans.append(S.count(str(i+1)))

print(max(Ans),min(Ans))
