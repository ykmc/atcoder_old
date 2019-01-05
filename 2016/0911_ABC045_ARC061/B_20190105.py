A = input()
B = input()
C = input()

# 文字列
S = {"a":A, "b":B, "c":C}
# 長さ
L = {"a":len(A), "b":len(B), "c":len(C)}
# 何文字目まで使ったか
C = {"a":0, "b":0, "c":0}

turn = "a"
# 文字を使い切る人が出るまで処理し続ける
while C[turn] < L[turn]:
    C[turn] += 1
    turn = S[turn][C[turn]-1]

print(turn.upper())

