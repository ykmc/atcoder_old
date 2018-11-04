N = int(input())
S = input()
pos = 0
minpos = 0
mini = 0
for i in range(N):
    if S[i]=="W":
        pos += 1
    else:
        pos -= 1
    if pos < minpos:
        minpos = pos
        mini = i

s1 = S[0:mini].count("W")
s2 = S[mini+1:N].count("E")
print(s1+s2)


