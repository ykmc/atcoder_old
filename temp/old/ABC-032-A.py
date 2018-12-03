import fractions
A = int(input())
B = int(input())
N = int(input())
lcm = A*B//fractions.gcd(A,B)
print((N-1)//lcm * lcm + lcm)