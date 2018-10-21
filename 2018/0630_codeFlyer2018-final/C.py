S = input()

Ans = 0
STACK = [1]

for c in S:
    if c == '(':
        # ( をスタックの階層で管理
        STACK.append(1)
    else:
        # 対応する ( がない場合はリセット
        if len(STACK) == 1:
            STACK[-1] = 1
        # 対応する ( がある場合
        else:
            # 対応する部分を取り出して計算
            STACK.pop()
            Ans += STACK[-1]
            STACK[-1] += 1

print(Ans)
