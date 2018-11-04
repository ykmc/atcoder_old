N = int(input())
limitN = 60000
P = [0]*limitN
listP = []
for i in range(2,limitN):
    if P[i] == 0:
        listP.append(i)
        j=1
        while i*j < limitN:
            P[i*j] = 1
            j+=1
Ans = list(map(str,filter(lambda x: x%5==1,listP)))
print(" ".join(Ans[0:N]))