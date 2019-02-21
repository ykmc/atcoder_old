S = input()

lenS = len(S)

ans = 9999
for i in range(lenS-2):
    if abs(int(S[i:i+3])-753) < abs(ans-753):
        ans = int(S[i:i+3])

print(abs(ans-753))