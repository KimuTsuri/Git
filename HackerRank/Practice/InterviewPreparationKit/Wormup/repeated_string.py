s = input()
n = int(input())
count = 0
amari = n % length
func_amari = 0
length = len(s)

for i in range(length):
    if s[i] == 'a':
        count += 1
    if s[i % length] in 'a' and amari :
        func_amari +=1

func = n // length
print( func * count + func_amari )


'''
#　time out
if len(s) == 1 and s == 'a':
    print(n)
else:
    for i in range(n):
        if s[ i % len(s)] == 'a':
            count += 1
    print(count)
'''