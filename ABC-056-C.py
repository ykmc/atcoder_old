X = int(input())
maxX = 0
for i in range(1,X+1):
    maxX += i
    if maxX >= X:
        print(i)
        break