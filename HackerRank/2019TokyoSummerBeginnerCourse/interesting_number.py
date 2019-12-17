a = int(input())
b = int(input())
ans = []

for i in range(a+1, b+1):
    if i % 3 ==0 and i % 5 ==0:
        continue
    elif i % 3 == 0 or i % 5 == 0:
        ans.append(i)


print(ans)
#message = map(str, ans)
#print('/n'.join(message))