N = int(input())
T = []
for i in range(N):
    T.append(input())

S = [0]*(12*24+1)
for  i in range(N):
    sh,sm = int(T[i][0:2]),int(T[i][2:4])
    eh,em = int(T[i][5:7]),int(T[i][7:9])
    sm = sm//5
    em = ((em-1)//5+1)
    start = sh*12 + sm
    end   = eh*12 + em
    S[start] += 1
    S[end]   -= 1

tmp,ans = 0,""
for i in range(len(S)):
    if tmp == 0 and S[i] > 0:
        ans = "{0:02d}".format(i//12) + "{0:02d}".format((i%12)*5)
    if tmp > 0 and tmp + S[i] == 0:
        ans += "-" + "{0:02d}".format(i//12) + "{0:02d}".format((i%12)*5)
        print(ans)
        ans = ""
    tmp += S[i]
