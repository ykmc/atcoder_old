N = int(input())
A = map(int,input().split())
rem = [3,0,1,0,1,2]
B = list(map(lambda x : rem[x%6], A))
print(sum(B))