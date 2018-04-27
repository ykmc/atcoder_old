N = int(input())
S = input()
L,R,x = 0,0,0
for i in range(N):
    if x == 0:
        if S[i]==")":
            L += 1
        else:
            R += 1
            x += 1
    else:
        if S[i]==")":
            R -= 1
            x -= 1
        else:
            R += 1
            x += 1
print("("*L + S + ")"*R)