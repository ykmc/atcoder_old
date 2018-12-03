N,K = map(int,input().split())
T = []
for i in range(N):
    T.append(list(map(int,input().split())))

def dfs(numQ,ans):
    if numQ==N:
        return ans==0
    for i in range(K):
        if(dfs(numQ+1, ans ^ T[numQ][i])):
            return True

print("Found" if dfs(0,0) else "Nothing")