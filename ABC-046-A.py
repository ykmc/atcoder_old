from collections import Counter
A,B,C = map(int,input().split())
print(len(Counter([A,B,C]).most_common()))