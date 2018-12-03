S = input()
T = "abcdefghijklmnopqrstuvwxyz"
for t in T:
    if t not in S:
        print(t)
        break
else:
    print("None")