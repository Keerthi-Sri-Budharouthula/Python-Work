Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
count=10
count=7
count
7
type(count)
<class 'int'>
price=99.99
price
99.99
type(price)
<class 'float'>
c=3+8j
c
(3+8j)
c=3+8J
c
(3+8j)
type(c)
<class 'complex'>
s='codegnan'
s
'codegnan'
type(s)
<class 'str'>
t="codegnan"
type(t)
<class 'str'>
l=[1,3,4,5]
>>> l
[1, 3, 4, 5]
>>> type(l)
<class 'list'>
>>> l.add(2)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    l.add(2)
AttributeError: 'list' object has no attribute 'add'
>>> t=(1,'tuple',9.99)
>>> t
(1, 'tuple', 9.99)
>>> type(t)
<class 'tuple'>
>>> s=set{}
SyntaxError: invalid syntax
>>> s={1,'set',8.3}
>>> s
{8.3, 1, 'set'}
>>> type(s)
<class 'set'>
>>> d={1,1,1,1}
>>> d
{1}
>>> d={'name':'sajid','batch':63,'course':'PFS'}
>>> d
{'name': 'sajid', 'batch': 63, 'course': 'PFS'}
>>> type(d)
<class 'dict'>
>>> b= True
>>> type(b)
<class 'bool'>
>>> 
>>> statue=None
>>> type(statue)
<class 'NoneType'>
>>> s=frozenset({1,2,3,4})
>>> s
frozenset({1, 2, 3, 4})
>>> type(s)
<class 'frozenset'>
