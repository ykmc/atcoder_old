H,W = map(int,input().split())
S = [input() for _ in range(H)]

print("#"*(W+2))
for i in range(H):
    print("#"+ S[i] +"#")
print("#"*(W+2))