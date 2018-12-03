N = int(input())
S = input()

S1,S2 = S[:N],S[N:][::-1]

dic = {}
keys = []
Ans = 0

for i in range(2**N):
    red,blue,red2,blue2 = "","","",""
    # 半分ずつbit全探索
    bits = bin(2**N+i)[3:]
    for j in range(N):
        if bits[j]=="0":
            red  += S1[j]
            red2 += S2[j]
        else:
            blue += S1[j]
            blue2 += S2[j]
    # あとで数える際に使うので記録しておく
    keys.append(red2+"-"+blue2)
    # 半分全列挙
    key = red+"-"+blue
    if key not in dic.keys():
        dic[key] = 1
    else:
        dic[key] += 1

for key in keys:
    Ans += dic.get(key,0)

print(Ans)