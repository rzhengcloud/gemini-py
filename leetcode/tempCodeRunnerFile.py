
a = "tzzzreea"

from collections import Counter
freq = Counter(a)
print(freq)
b = sorted(freq.items(), key = lambda x : (-x[1], x[0]))
print(b)

c = sorted(freq.items(), key = lambda x : (x[1], x[0]))
print(c)

print(*(val for val, f in freq.items()))

v = [[5,'a'],[4,'e'],[6,'c']]
print(v)
v.sort(key = lambda x : x[1])

print(v)
