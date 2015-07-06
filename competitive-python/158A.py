n, k = map(int, raw_input().split())
s = map(int,raw_input().split())
list = [x>=max(s[k-1],1) for x in s]
print sum(list)