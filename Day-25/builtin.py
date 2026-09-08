
import sys
#print(sys.path)
#print(sys.version)
print("Start")
sys.exit()
print("End")


import platform
print(platform.system())
print(platform.release())
print(platform.processor())


import math

print(math.pi)
print(math.e)

print(math.sqrt(36))
print(math.pow(2,3))

print(math.ceil(12.00001))
print(math.ceil(12.3))
print(math.ceil(12.6))
print(math.ceil(12.99999))

print(math.floor(12.00001))
print(math.floor(12.3))
print(math.floor(12.6))
print(math.floor(12.99999))

print(math.fabs(-10))
print(math.factorial(5))
print(math.gcd(8,24))
print(math.log(2,2))
print(math.sin(30))
print(math.cos(30))
print(math.tan(30))
print(math.degrees(30))
print(math.radians(30))


import random
#random.seed(10)

print(random.randint(1,10))
print(random.randint(100000,999999))
print(random.random())
print(random.uniform(1,6))

l=['R','P','S']
print(random.choice(l))
print(random.choices(l,k=2))

random.shuffle(l)
print(l)


from collections import Counter

s='python programming'
m= 'this is that that is this is is'.split()
l= [1,1,1,1,2,3,4,5,45,123,12,23,1,21,32,3,4,1,32,4,5]

print(Counter(s))
print(Counter(m))
print(Counter(l))


from collections import defaultdict
s='python programming'
m= 'this is that that is this is is'.split()
l= [1,1,1,1,2,3,4,5,45,123,12,23,1,21,32,3,4,1,32,4,5]

d=defaultdict(int)
for i in s:
    d[i]+=1

print(d)


from collections import deque

l=deque()

l.append(10)
l.append(20)
l.append(30)
l.popleft()
l.popleft()
l.append(50)
l.append(70)
l.popleft()


l.appendleft(10)
l.appendleft(20)
l.appendleft(30)
l.pop()
l.pop()
l.appendleft(50)
l.appendleft(70)
l.pop()

print(l)



from itertools import combinations, permutations
print(list(combinations('abc',2)))
print(list(permutations('abc',2)))

res1=list(combinations('abc',2))
res2=list(permutations('abc',2))

print([''.join(i) for i in res1 ])
print([''.join(i) for i in res2])



































































