Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a=10
>>> A=20
>>> a
10
>>> A
20
>>> a=10
>>> a=b=c
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    a=b=c
NameError: name 'c' is not defined
>>> a=b=c=10
>>> a
10
>>> b
10
>>> c
10
>>> a,b,c=10,20,30
>>> a
10
>>> b
20
>>> c
30
>>> a=10
>>> b=20
>>> a,b=b,a
>>> a
20
>>> b
10
