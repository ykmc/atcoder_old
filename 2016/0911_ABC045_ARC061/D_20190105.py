H,W,N = map(int,input().split())
dic = {}
for i in range(N):
    a,b = map(int,input().split())
    for dh in range(3):
        for dw in range(3):
            if 0<a-dh<=H-2 and 0<b-dw<=W-2:
                if (a-dh,b-dw) not in dic.keys():
                    dic[(a-dh,b-dw)] = 1
                else:
                    dic[(a-dh,b-dw)] += 1

Ans = [0]*10
total = 0
for v in dic.values():
    Ans[v] += 1
    total += 1

Ans[0] = (H-2)*(W-2) - total

for ans in Ans:
    print(ans)

