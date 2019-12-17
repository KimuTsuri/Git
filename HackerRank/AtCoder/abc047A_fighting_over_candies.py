abc_candies = list(map(int, input().split()))
a = abc_candies[0]
b = abc_candies[1]
c = abc_candies[2]

if a == b + c:
    print('Yes')
elif b == c + a:
    print('Yes')
elif c == a + b:
    print('Yes')
else:
    print('No')