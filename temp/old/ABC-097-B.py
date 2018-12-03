X = int(input())

s = [1]
for i in range(X+1):
    for j in range(2,X+1):
        if i**j <= X and i**j not in s:
            s.append(i**j)
        if i**j > X:
            break
print(max(s)) 