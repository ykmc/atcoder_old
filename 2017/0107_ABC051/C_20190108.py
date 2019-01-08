sx,sy,tx,ty = map(int,input().split())

dx = tx-sx
dy = ty-sy

Ans = "U"*dy + "R"*dx + "D"*dy + "L"*dx
Ans += "L" + "U"*(dy+1) + "R"*(dx+1) + "D"
Ans += "R" + "D"*(dy+1) + "L"*(dx+1) + "U"

print(Ans)