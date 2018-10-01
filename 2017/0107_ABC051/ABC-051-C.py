Sx,Sy,Tx,Ty = map(int,input().split())
Dx,Dy = abs(Tx-Sx),abs(Ty-Sy)
S = ""

moveX,moveY = [],[]
if Dx > 0:
    moveX = ["R","L","R","L"] 
elif Dx < 0:
    moveX = ["L","R","L","R"]
if Dy > 0:
    moveY = ["U","D","U","D"]
elif Dy < 0:
    moveY = ["D","U","D","U"]

S += moveY[0]*Dy + moveX[0]*Dx
S += moveY[1]*Dy + moveX[1]*Dx
S += moveX[1] + moveY[0]*(Dy+1) + moveX[0]*(Dx+1) + moveY[1]
S += moveX[0] + moveY[1]*(Dy+1) + moveX[1]*(Dx+1) + moveY[0]

print(S)
