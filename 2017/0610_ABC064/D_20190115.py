N = int(input())
S = input()

# "("*L + S + ")"*R
L,R = 0,0
# 余っている "(" の個数 
rem = 0

for s in S:
    # ")"
    if s==")":
        if rem==0:
            L += 1
        else:
            R -= 1
            rem -= 1
    # "("
    else:
        R += 1
        rem += 1

print("("*L + S + ")"*R) 