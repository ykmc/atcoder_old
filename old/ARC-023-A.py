y = int(input())
m = int(input())
d = int(input())

from math import floor

def calc(y,m,d):
    if m in (1,2):
        m += 12
        y -= 1
    return 365*y + floor(y/4) - floor(y/100) + floor(y/400) + floor(306*(m+1)/10) + d -429

print(calc(2014,5,17) - calc(y,m,d))