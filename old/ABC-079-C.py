S = input()
OPs =["+++","++-","+-+","+--","-++","-+-","--+","---"]
for op in OPs:
    if eval(S[0]+op[0]+S[1]+op[1]+S[2]+op[2]+S[3]) == 7:
        print(S[0]+op[0]+S[1]+op[1]+S[2]+op[2]+S[3]+"=7")
        break