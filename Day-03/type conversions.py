Python 3.14.3 (tags/v3.14.3:32c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
int
<class 'int'>
i=10
type(i)
<class 'int'>
float(i)
10.0
complex(i)
(10+0j)
str(i)
'10'
list(i)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    list(i)
TypeError: 'int' object is not iterable
tuple(i)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    tuple(i)
TypeError: 'int' object is not iterable
set(i)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    set(i)
TypeError: 'int' object is not iterable
dict(i)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    dict(i)
TypeError: 'int' object is not iterable
bool(i)
True

f=10.2
int(f)
10
complex(f)
(10.2+0j)
str(f)
'10.2'
list(f)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    list(f)
TypeError: 'float' object is not iterable
tuple(f)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    tuple(f)
TypeError: 'float' object is not iterable
set(f)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    set(f)
TypeError: 'float' object is not iterable
dict(f)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    dict(f)
TypeError: 'float' object is not iterable
bool(f)
True

c=10+3j
int(c)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    int(c)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
float(c)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    float(c)
TypeError: float() argument must be a string or a real number, not 'complex'
str(c)
'(10+3j)'
list(c)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    list(c)
TypeError: 'complex' object is not iterable
tuple(c)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    tuple(c)
TypeError: 'complex' object is not iterable
set(c)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    set(c)
TypeError: 'complex' object is not iterable
dict(c)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    dict(c)
TypeError: 'complex' object is not iterable
bool(c)
True

s='codegnan'
int(s)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    int(s)
ValueError: invalid literal for int() with base 10: 'codegnan'
float(s)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    float(s)
ValueError: could not convert string to float: 'codegnan'
complex(s)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    complex(s)
ValueError: complex() arg is a malformed string
list(s)
['c', 'o', 'd', 'e', 'g', 'n', 'a', 'n']
tuple(s)
('c', 'o', 'd', 'e', 'g', 'n', 'a', 'n')
set(s)
{'g', 'c', 'n', 'o', 'd', 'e', 'a'}
dict(s)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    dict(s)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
bool(s)
True

l=[1,3.3,5,'data']
int(l)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    int(l)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
float(l)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    float(l)
TypeError: float() argument must be a string or a real number, not 'list'
complex(l)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    complex(l)
TypeError: complex() argument must be a string or a number, not list
tuple(l)
(1, 3.3, 5, 'data')
set(l)
{1, 3.3, 5, 'data'}
dict(l)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    dict(l)
TypeError: object is not iterable
Cannot convert dictionary update sequence element #0 to a sequence
>>> bool(l)
True
>>> 
>>> t=(1,2.0,'tuple',{1,2,3])
SyntaxError: closing parenthesis ']' does not match opening parenthesis '{'
>>> t=(1,2.0,'tuple',[1,2,3])
>>> int(t)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    int(t)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'tuple'
>>> float(t)
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    float(t)
TypeError: float() argument must be a string or a real number, not 'tuple'
>>> complex(t)
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    complex(t)
TypeError: complex() argument must be a string or a number, not tuple
>>> set(t)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    set(t)
TypeError: cannot use 'list' as a set element (unhashable type: 'list')
>>> str(t)
"(1, 2.0, 'tuple', [1, 2, 3])"
>>> dict(t)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    dict(t)
TypeError: object is not iterable
Cannot convert dictionary update sequence element #0 to a sequence
>>> bool(t)
True
>>> list(t)
[1, 2.0, 'tuple', [1, 2, 3]]
>>> type(t)
<class 'tuple'>
>>> s={1,2.3,'set',(1,2,3)}


