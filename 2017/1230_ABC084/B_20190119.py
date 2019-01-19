A,B = map(int,input().split())
S = input()

print("Yes" if len(S)==A+B+1 and S.count("-")==1 and S[A]=="-" else "No")