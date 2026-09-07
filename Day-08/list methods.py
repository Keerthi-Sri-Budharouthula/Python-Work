Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
l=[1,2,3,4,5]
l=[10,9,6,1,2,3,4]
l
[10, 9, 6, 1, 2, 3, 4]
id(l)
2299797926592
l.append(12)
l
[10, 9, 6, 1, 2, 3, 4, 12]
l.append(14)
l
[10, 9, 6, 1, 2, 3, 4, 12, 14]
id(l)
2299797926592
l.insert(1,13)
l
[10, 13, 9, 6, 1, 2, 3, 4, 12, 14]
l.extend([52,32,42])
l
[10, 13, 9, 6, 1, 2, 3, 4, 12, 14, 52, 32, 42]
id(l)
2299797926592
l[3]
6
l[3]=60
l
[10, 13, 9, 60, 1, 2, 3, 4, 12, 14, 52, 32, 42]
l[5]=20
l
[10, 13, 9, 60, 1, 20, 3, 4, 12, 14, 52, 32, 42]
id(l)
2299797926592
l.pop()
42
l
[10, 13, 9, 60, 1, 20, 3, 4, 12, 14, 52, 32]
l.pop()
32
l.pop(1)
13
l
[10, 9, 60, 1, 20, 3, 4, 12, 14, 52]
l.pop(2)
60
l
[10, 9, 1, 20, 3, 4, 12, 14, 52]
l.remove(4)
l
[10, 9, 1, 20, 3, 12, 14, 52]
del l[1]
l
[10, 1, 20, 3, 12, 14, 52]
l.clear()
l
[]
id(l)
2299797926592

l=[10, 1, 20, 3, 12, 14]
l
[10, 1, 20, 3, 12, 14]
max(l)
20
min(l)
1
sorted(l)
[1, 3, 10, 12, 14, 20]
l
[10, 1, 20, 3, 12, 14]
l.reverse()
l
[14, 12, 3, 20, 1, 10]
l.sort()
l
[1, 3, 10, 12, 14, 20]
l.sort(reverse=True)
l
[20, 14, 12, 10, 3, 1]
sum(l)
60
l=[1,2,3]
m=[1,2,3]
l
[1, 2, 3]
n=l
n.append(4)
n
[1, 2, 3, 4]
l
[1, 2, 3, 4]
m=l.copy()
m
[1, 2, 3, 4]
m.append(10)
m
[1, 2, 3, 4, 10]
l
[1, 2, 3, 4]
all([0,'',[],(),set(),{},False])
False
all([1,0,'',[],(),set(),{},False])
False
any([1,0,'',[],(),set(),{},False])
True
>>> 
>>> l
[1, 2, 3, 4]
>>> l.index(3)
2
>>> l.index(5)
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    l.index(5)
ValueError: list.index(x): x not in list
>>> l
[1, 2, 3, 4]
>>> l.count(3)
1
>>> l.count(5)
0
>>> 
>>> l
[1, 2, 3, 4]
>>> l[[1,2,3,4],[5,6,7,8]]
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    l[[1,2,3,4],[5,6,7,8]]
TypeError: list indices must be integers or slices, not tuple
>>> l=[[1,2,3,4],[5,6,7,8]]
>>> l
[[1, 2, 3, 4], [5, 6, 7, 8]]
>>> l[0]
[1, 2, 3, 4]
>>> l[1]
[5, 6, 7, 8]
>>> l[0][2]
3
>>> l[1][3]
8
>>> l[-1][-1]
8
>>> 
