import collections

ar = list(map(int, input().rstrip().split()))

c = collections.Counter(ar)
value_list = list(c.values())

count = 0
for i in range(len(value_list)):
    count += value_list[i]//2
print(count)