s=input()
s=s.strip()
s=s.lower()
s='.'.join([l for l in s if l not in ['a','e','i','o','u','y']])
print'.'+s
