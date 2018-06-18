N = int(input())
B = [[] for i in range(N)]
for i in range(1,N):
    b = int(input()) - 1
    B[b].append(i)

def dfs(list):
    if len(list) == 0:
        return 1
    else:
        salary = []
        for l in list:
            salary.append(dfs(B[l]))
        return max(salary) + min(salary) + 1

print(dfs(B[0]))
