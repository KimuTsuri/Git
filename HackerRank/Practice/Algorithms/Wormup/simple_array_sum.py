ar = list(map(int, input().rstrip().split()))
count = 0
for i in range(len(ar)):
    count += ar[i]
print(count)