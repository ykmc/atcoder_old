S = input()

if (S[0]==S[-1]) ^ (len(S)%2==0):
    print("Second")
else:
    print("First")