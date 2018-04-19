from math import ceil
A,B,C,D,E,F = map(int,input().split())

W,S = [],[0]

for ai in range(ceil(F/A)):
    for bi in range(ceil(F/B)):
        w = 100*A*ai+100*B*bi
        if w <= F and 0 < w and w not in W:
            W.append(w)
for ci in range(ceil(F/C)):
    for di in range(ceil(F/D)):
        s = C*ci+D*di
        if s <= F and 0 < s and s not in S:
            S.append(s)

AnsWS,AnsS,r = 0,0,-1
for wi in W:
    for si in S:
        if r < si/wi and si <= E*(wi//100) and (wi+si) <= F:
            AnsWS,AnsS,r = wi+si,si,si/wi

print(AnsWS,AnsS)