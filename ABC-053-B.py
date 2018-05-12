S = input()
print(len(S) -S[::-1].find("Z") -S.find("A"))