
a = "tzzzreea"

from collections import Counter
freq = Counter(a)
print(freq)
#primary sort - largest to smallest. 
#secondary sort - x[0] smallest to largest 
b = sorted(freq.items(), key = lambda x : (-x[1], x[0]))
print(b)

c = sorted(freq.items(), key = lambda x : (x[1], x[0]))
print(c)

print(*(val for val, f in freq.items()))

v = [[5,'a'],[4,'e'],[6,'c']]
print(v)
v.sort(key = lambda x : x[1])

print(v)



from collections import Counter

s = "helloaaaa"

count = Counter(s)

print(count)

for key in count:
    print(f"{key=}")
    
# for key, val in count.items():
#     print(f"{key=}, {val=}")

# count = sorted(count.items(), key = lambda x: x[1])
# print(count)

# del count['o']

# print(count)