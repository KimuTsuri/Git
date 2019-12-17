s = input()
a = -1
b = -1

if len(s) == 2:
    if s[0] == s[1]:
        a = 1
        b = 2
else:
    for i in range(len(s)-2):
        if s[i] == s[i+1]:
            a = i+1
            b = i+2
            break
        if s[i] == s[i+2]:
            a = i+1
            b = i+3
            break
print(a, b)