n = int(input())
c = list(map(int, input().rstrip().split()))
i = 0
jumps = 0

while i < n-1:
    i += (c[i] == 0) + 1
    jumps += 1
print(jumps)
