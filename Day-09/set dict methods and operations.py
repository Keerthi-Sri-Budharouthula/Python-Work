Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s={}
type(s)
<class 'dict'>
s=set()
s={1,2,3,44,54,8,57854}
s
{1, 2, 3, 54, 8, 44, 57854}
s=set()
s
set()
s.add(1)

s
{1}
s.add(1)
s.add(12.3)
s.add(2+4j)
s.add("str")
s.add([1,2,3])
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    s.add([1,2,3])
TypeError: cannot use 'list' as a set element (unhashable type: 'list')
s={False,1,'str',(1,2,3),12.3,(2+4j)}
s
{False, 1, 'str', (1, 2, 3), 12.3, (2+4j)}
s{1,1,1,1,1,1}
SyntaxError: invalid syntax
s
{False, 1, 'str', (1, 2, 3), 12.3, (2+4j)}
s={1,1,1,1,1,1}
s
{1}
l={10,20,30}
m={1,2,3,4}
1+m
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    1+m
TypeError: unsupported operand type(s) for +: 'int' and 'set'
a={1,2,3,4,5}
b={3,5,7,9}
a
{1, 2, 3, 4, 5}
b
{9, 3, 5, 7}
a|b
{1, 2, 3, 4, 5, 7, 9}
a & b
{3, 5}
a - b
{1, 2, 4}
a^b
{1, 2, 4, 7, 9}
a>={1,2,3}
True
a>={7,9}
False
{1}<=a
True
{9}<=b
True
a.isdisjoint(b)
False
a.isjoint(b)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    a.isjoint(b)
AttributeError: 'set' object has no attribute 'isjoint'. Did you mean: 'isdisjoint'?
a.isdisjoint(b)
False
a. union(b)
{1, 2, 3, 4, 5, 7, 9}
a.intersection(b)
{3, 5}
(1,2,3}.in(a)
SyntaxError: closing parenthesis '}' does not match opening parenthesis '('
{1,2,3}in(a)
False
a.isdisjoint({9,10})
True
a.issubset(b)
False
a.superset(b)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    a.superset(b)
AttributeError: 'set' object has no attribute 'superset'. Did you mean: 'issuperset'?
a.issuperset(b)
False
a
{1, 2, 3, 4, 5}
5 in a
True
9 in a
False
9 in b
True
9 not in a
True

#set Methods
max(a)
5
min(a)
1
sorted(a)#always get list
[1, 2, 3, 4, 5]
sum(a)
15
a
{1, 2, 3, 4, 5}
b=a
b
{1, 2, 3, 4, 5}
b.add(12)
b
{1, 2, 3, 4, 5, 12}
a
{1, 2, 3, 4, 5, 12}
c=a.copy()
c.add(12)
c.add(13)
c
{1, 2, 3, 4, 5, 12, 13}
a
{1, 2, 3, 4, 5, 12}
a.add(123)#add single element
a
{1, 2, 3, 4, 5, 123, 12}
a.update({16,17,18})#add nultiple elements
a
{1, 2, 3, 4, 5, 12, 16, 17, 18, 123}
a.pop()
1
a.pop()
2
a
{3, 4, 5, 12, 16, 17, 18, 123}
a.pop()
3
a.remove(16)
a
{4, 5, 12, 17, 18, 123}
a.remove(12)
a
{4, 5, 17, 18, 123}
a.remove(12)
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    a.remove(12)
KeyError: 12
a.discard(12)
a.discard(5)
a
{4, 17, 18, 123}
a.discard(5)
a.clear()
a
set()
a={1,2,4,5}
a.update({"str",0,12,13,-1,-23.4})
a
{0, 1, 2, 4, 5, 'str', -23.4, 12, 13, -1}
len(a)
10
all(a)
False
any(a)
True
a=frozenset({"str",0,12,13,-1,-23.4})
a
frozenset({0, 'str', -23.4, 12, 13, -1})
a.add(12)
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    a.add(12)
AttributeError: 'frozenset' object has no attribute 'add'
d={}
d=dict()
type(d)
<class 'dict'>
d={'k1':'v1','k2':'v2','k3':'v3'}
d
{'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}
id(d)
1456743829824
d['k4']='v4'
d
{'k1': 'v1', 'k2': 'v2', 'k3': 'v3', 'k4': 'v4'}
id(d)
1456743829824
d['k1']='v11'
d
{'k1': 'v11', 'k2': 'v2', 'k3': 'v3', 'k4': 'v4'}
d['k5']='v4'
d
{'k1': 'v11', 'k2': 'v2', 'k3': 'v3', 'k4': 'v4', 'k5': 'v4'}
d={}
d[1]='int'
d
{1: 'int'}
d[12.3]='float'
d
{1: 'int', 12.3: 'float'}
d[2+3j]='complex'
d
{1: 'int', 12.3: 'float', (2+3j): 'complex'}
d['str']='string'
d
{1: 'int', 12.3: 'float', (2+3j): 'complex', 'str': 'string'}
d[(1,2,3,4)]='tuple'
d
{1: 'int', 12.3: 'float', (2+3j): 'complex', 'str': 'string', (1, 2, 3, 4): 'tuple'}
d=
SyntaxError: invalid syntax
d={}
d[1]=1
d[2]=12.3
d[3]=12+4j
d[4]='str'
d[5]=[1,2,3,4]
d[6]=(1,2,3)
d[7]={1,2,3}
d[8]={1:1}
d[9]=True
>>> d
{1: 1, 2: 12.3, 3: (12+4j), 4: 'str', 5: [1, 2, 3, 4], 6: (1, 2, 3), 7: {1, 2, 3}, 8: {1: 1}, 9: True}
>>> 9 in d
True
>>> 10 in d
False
>>> 'str' in d
False
>>> d[5]
[1, 2, 3, 4]
>>> d[8]
{1: 1}
>>> d[10]
Traceback (most recent call last):
  File "<pyshell#138>", line 1, in <module>
    d[10]
KeyError: 10
>>> d.get(10)
>>> d.get(1)
1
>>> d.get(10,"Key is not present")
'Key is not present'
>>> d
{1: 1, 2: 12.3, 3: (12+4j), 4: 'str', 5: [1, 2, 3, 4], 6: (1, 2, 3), 7: {1, 2, 3}, 8: {1: 1}, 9: True}
>>> d.get(6,"key is not present")
(1, 2, 3)
>>> d[5]=10
>>> d
{1: 1, 2: 12.3, 3: (12+4j), 4: 'str', 5: 10, 6: (1, 2, 3), 7: {1, 2, 3}, 8: {1: 1}, 9: True}
>>> d[6]=12
>>> d
{1: 1, 2: 12.3, 3: (12+4j), 4: 'str', 5: 10, 6: 12, 7: {1, 2, 3}, 8: {1: 1}, 9: True}
>>> d[7]=20
>>> d
{1: 1, 2: 12.3, 3: (12+4j), 4: 'str', 5: 10, 6: 12, 7: 20, 8: {1: 1}, 9: True}
