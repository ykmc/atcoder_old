R,G,B = map(int,input().split())
print("YES" if (R*100+G*10+B)%4==0 else "NO")