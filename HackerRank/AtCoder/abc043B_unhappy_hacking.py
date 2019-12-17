s = input()
output = []

for n in range(len(s)):
    if s[n] == '1' or s[n] == '0':
        output.append(s[n])
    elif s[n] == 'B' and output != []:
        backspace = len(output)-1
        output = output[:backspace]
print(''.join(output))

