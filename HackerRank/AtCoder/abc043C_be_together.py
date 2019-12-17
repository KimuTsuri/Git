N = int(input())
a = list(map(int,input().split()))

cost = []
for i in range(-100, 101):
    cost_all = 0
    for j in a:
        cost_all += (j - i) ** 2
    cost.append(cost_all)

print(min(cost))
