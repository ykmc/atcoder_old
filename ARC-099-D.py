K = int(input())

Ans = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for x in range(1,15):
    B = [0]*100000
    n,d = 10**x,int("9"*x)
    for i in range(10000):
        num = i*n+d
        S = str(num)
        total = 0
        for s in S:
            total += int(s)
        B[i] = num/total
        if i > 0:
            if B[i] < B[i-1]:
                #最後の値を削除
                Ans.pop()
                break
            else:
                if num not in Ans:
                    Ans.append(num)

for i in range(K):
    print(Ans[i])