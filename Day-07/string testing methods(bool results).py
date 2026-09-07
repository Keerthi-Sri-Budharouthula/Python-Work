Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
c = 'strings.py'
c.startswith('str')
True
c.sartwith('python')
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    c.sartwith('python')
AttributeError: 'str' object has no attribute 'sartwith'. Did you mean: 'startswith'?
c.sartswith('python')
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    c.sartswith('python')
AttributeError: 'str' object has no attribute 'sartswith'. Did you mean: 'startswith'?
>>> c.startswith('python')
False
>>> c.endswith('python')
False
>>> c.endswith('py')
True
>>> c.islower()
True
>>> c.isupper()
False
>>> 'PYTHONV13'.isupper()
True
>>> c.isalpha()
False
>>> c.isalnum()
False
>>> 's123'.isalnum()
True
>>> 's.123'.isalnum()
False
>>> '      '.isspace()
True
>>> 'h      '.isspace()
False
>>> 'this is title'.istitle()
False
>>> 'This Is Title'.istitle()
True
>>> 'my@var'.isidentifier()
False
>>> 'my_var'.isidentifier()
True
>>> 
>>> 
