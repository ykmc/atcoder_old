Xa,Ya,Xb,Yb,Xc,Yc = map(int,input().split())

X1,Y1,X2,Y2 = Xb-Xa,Yb-Ya,Xc-Xa,Yc-Ya
print(abs(X1*Y2-X2*Y1)*0.5)