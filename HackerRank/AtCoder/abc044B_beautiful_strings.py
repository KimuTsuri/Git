import string
w = input()
if all([w.count(low_alpha) % 2 == 0 for low_alpha in string.ascii_lowercase ]):
    print('Yes')
else:
    print('No')