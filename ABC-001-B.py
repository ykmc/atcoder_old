m = int(input())

Ans = ""
if m<100:
    Ans = "00"
elif m<6000:
    Ans = "{0:02d}".format(m//100)
elif m<35000:
    Ans = m//1000+50
elif m<=70000:
    Ans = (m//1000-30)//5+80
else:
    Ans = 89

print(Ans)