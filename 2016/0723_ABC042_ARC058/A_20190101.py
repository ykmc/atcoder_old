ABC = list(map(int,input().split()))

# 5が2つ、7が1つあれば良いので
print("YES" if ABC.count(5)==2 and ABC.count(7)==1 else "NO")