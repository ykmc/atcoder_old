A,B = map(int,input().split())
A = (A+11)%13
B = (B+11)%13

ans = "Draw"
if A>B:
    ans = "Alice"
elif A<B:
    ans = "Bob"

print(ans)