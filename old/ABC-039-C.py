S = input()
T = ["WB","WB","W","WB","WB","WB","W","WB","WB","W","WB","WB","WB","W"]
Ans = ["Do","Re","Mi","Fa","So","La","Si"]
for i in range(len(Ans)):
    joinT = "".join(T)
    if S == joinT[0:20]:
        break
    else:
        t0 = T[0]
        T = T[1:]
        T.append(t0)
print(Ans[i])