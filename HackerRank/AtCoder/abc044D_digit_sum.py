import sys, math
n = int(input())
s = int(input())

def f(b, n):
    if n < b:
        return n
    else:
        return f(b, n//b) + n % b

if s == n:
    print(n + 1)
    sys.exit()

sqrt_n = math.floor(math.sqrt(n))
for b in range(2, sqrt_n + 1):
    if f(b, n) == s:
        print(b)
        sys.exit()
for p in range(1, sqrt_n + 1):
    p_sum= sqrt_n + 1 - p
    b = int( (n -s)/p_sum ) + 1
    if b >= 2 and f(b, n) == s:
        print(b)
        sys.exit()
print('-1')