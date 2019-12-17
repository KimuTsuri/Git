s = input()

list_s = list(s)

step = 0
prvi = 0
count =0

for i in range(len(list_s)):
    prvi = step
    if list_s[i] == 'U':
        step += +1
    if list_s[i] == 'D':
        step += -1
    if prvi < 0:
        if step == 0:
            count +=1

print(count)
