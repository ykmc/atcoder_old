N = int(input())
S = input()

B = {"S":"W", "W":"S"}
def check(a0, a1):
    b0,b1 = a0,a1
    A = a1
    for i in range(N):
        if a1 == "S":
            if S[i] == "o":
                a2 = a0
            else:
                a2 = B[a0]
        else:
            if S[i] == "o":
                a2 = B[a0]
            else:
                a2 = a0
        A += a2
        a0,a1 = a1,a2
    if A[0] == A[N] and A[0] == b1 and A[N-1] == b0:
        return A[0:N]
    else:
        return -1

Ans = []
Ans.append(check("S","S"))
Ans.append(check("S","W"))
Ans.append(check("W","S"))
Ans.append(check("W","W"))

for ans in Ans:
    if ans == -1:
        continue
    else:
        print(ans)
        exit()
else:
    print(-1)


