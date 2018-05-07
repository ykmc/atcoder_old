X = int(input())
print((X-1)//11*2+2 if (X-1)%11>5 else (X-1)//11*2+1)