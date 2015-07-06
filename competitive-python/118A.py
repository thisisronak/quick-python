s = ''
for c in raw_input().lower():
    if c in 'bcdfghjklmnpqrstvwxz':
        s += '.' + c
print s