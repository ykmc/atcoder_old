A,B,C,D = map(int,input().split())
takahashi = B/A
aoki = D/C
if takahashi > aoki:
    print("TAKAHASHI")
elif aoki > takahashi:
    print("AOKI")
elif takahashi == aoki:
    print("DRAW")