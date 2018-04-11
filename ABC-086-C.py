N = int(input())
S = "Yes"
A = [(0,0,0)]
for i in range(N):
    t,x,y = map(int,input().split())
    A.append((t,x,y))
A = sorted(A)
for i in range(N):
    t1,x1,y1 = A[i]
    t2,x2,y2 = A[i+1]
    if abs(x2-x1)+abs(y2-y1) > t2-t1  or   (abs(x2-x1)+abs(y2-y1))%2 != (t2-t1)%2:
        S = "No"
        break
print(S)