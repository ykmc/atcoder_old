S = input().split("/")

# 閏年
def check_leap(Y):
    ret = False
    if Y%4==0:
        ret = True
    if Y%100==0:
        ret = False
    if Y%400==0:
        ret = True
    return ret

# 頭の0をとって数字に
for i,s in enumerate(S,0):
    while s[0]==0:
        s = s[1:]
    S[i] = int(s)

Y,M,D = S[0],S[1],S[2]
while (Y/M)/D != (Y/M)//D:
    # 日付の最大値
    D_MAX = 31
    if M in [4,6,9,11]:
        D_MAX = 30
    elif M in [2]:
        if check_leap(Y):
            D_MAX = 29
        else:
            D_MAX = 28
    
    if D == D_MAX:
        D = 1
        if M == 12:
            M = 1
            Y += 1
        else:
            M += 1
    else:
        D += 1

print("{:04d}/{:02d}/{:02d}".format(Y,M,D))