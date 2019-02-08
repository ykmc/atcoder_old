S = input()
Ans = 0
half = len(S)//2
for i in range(1,half):
    if S[0:half-i]==S[half-i:len(S)-i*2]:
        Ans = (half-i)*2
        break

print(Ans)