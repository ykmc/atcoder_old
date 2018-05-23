X = input()
Y = X.replace("ch","").replace("o","").replace("k","").replace("u","")
print("YES" if len(Y)==0 else "NO")