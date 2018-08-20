C,D = map(int,input().split())

Ans = 0
bpml,bpmh = 140,170
while bpml <= D:
    Ans += max(min(bpmh,D)-max(bpml,C),0)
    bpml *= 2
    bpmh *= 2

print(Ans)