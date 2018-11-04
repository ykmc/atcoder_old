ss = input()

ans = ""
dic = {"O":0, "D":0, "I":1, "Z":2, "S":5, "B":8}
for s in ss:
    if s not in "0123456789":
        ans += str(dic[s])
    else:
        ans += str(s)

print(ans)
