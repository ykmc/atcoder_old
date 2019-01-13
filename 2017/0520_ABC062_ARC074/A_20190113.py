X,Y = map(int,input().split())

Ans = "No"
A = [[1,3,5,7,8,10,12],[4,6,9,11],[2]]
for i in range(3):
    if X in A[i] and Y in A[i]:
        Ans = "Yes"

print(Ans)