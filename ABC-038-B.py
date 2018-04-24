H1,W1 = map(int,input().split())
H2,W2 = map(int,input().split())
print("YES" if H1 in (H2,W2) or W1 in (H2,W2) else "NO")