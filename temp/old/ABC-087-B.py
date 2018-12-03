A,B,C,X = int(input()),int(input()),int(input()),int(input())
n = 0
for i in range(0,A+1):
    for j in range(0,B+1):
        for k in range(0,C+1):
            if 500*i+100*j+50*k == X:
                n+=1
print(n)