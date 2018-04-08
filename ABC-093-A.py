S = input()
for c in ("abc"):
    if c in S:
        continue
    else:
        print("No")
        exit()
print("Yes")