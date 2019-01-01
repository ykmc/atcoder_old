N,L = map(int,input().split())
S = []
for i in range(N):
    s = input()
    S.append(s)

# pythonは文字列の場合は辞書順を考慮してsortしてくれる
S.sort()

print("".join(S))