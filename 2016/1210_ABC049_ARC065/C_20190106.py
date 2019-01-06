import sys
S = input()
S = S[::-1]

AR = []
A = ["dream","dreamer","erase","eraser"]
for a in A:
    AR.append(a[::-1])

i = 0
while i < len(S):
    for ar in AR:
        l = len(ar)
        if ar == S[i:i+l]:
            i += l
            break
    else:
        print("NO")
        sys.exit()

print("YES")

