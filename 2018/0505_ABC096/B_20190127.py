A,B,C = map(int,input().split())
K = int(input())
maxV = max(A,B,C)
print(A+B+C-maxV+maxV*2**K)