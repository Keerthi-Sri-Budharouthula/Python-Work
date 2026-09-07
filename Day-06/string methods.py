Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
c= 'python programming'
len(c)
18
ord('p')
112
ord('a')
97
ord('0')
48
ord('A')
65
chr('A')
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    chr('A')
TypeError: 'str' object cannot be interpreted as an integer
chr(65)
'A'
'A'chr(97)
SyntaxError: invalid syntax
chr(97)
'a'
min('c')
'c'
min(c)
' '
max(c)
'y'
sorted(c)
[' ', 'a', 'g', 'g', 'h', 'i', 'm', 'm', 'n', 'n', 'o', 'o', 'p', 'p', 'r', 'r', 't', 'y']
chr(66)
'B'
chr(56)
'8'
chr(77)
'M'
sorted(b)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    sorted(b)
NameError: name 'b' is not defined
sorted(c)
[' ', 'a', 'g', 'g', 'h', 'i', 'm', 'm', 'n', 'n', 'o', 'o', 'p', 'p', 'r', 'r', 't', 'y']
c= 'String is immutable'
c
'String is immutable'
c.title()
'String Is Immutable'
c.swapcase()
'sTRING IS IMMUTABLE'
c.lower()
'string is immutable'
c.upper()
'STRING IS IMMUTABLE'
c.capitalize()
'String is immutable'
"STRAẞEMÁLAGAÅngströmCafé".casefold()
'strassemálagaångströmcafé'
c
'String is immutable'
c.center(60,'0')
'00000000000000000000String is immutable000000000000000000000'
c.ljust(60,'@')
'String is immutable@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
c.rjust(60,'$')
'$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$String is immutable'
'12'.zfill(4)
'0012'
'12345'.zfill(6)
'012345'
'9838987'.zfill(10)
'0009838987'
c
'String is immutable'
c.find
<built-in method find of str object at 0x0000027D2C746AF0>
c.find('s')
8
c.finf('S')
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    c.finf('S')
AttributeError: 'str' object has no attribute 'finf'. Did you mean: 'find'?
c.find('S')
0
c.find('i')
3
c.finf('z')
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    c.finf('z')
AttributeError: 'str' object has no attribute 'finf'. Did you mean: 'find'?
c.find('z')
-1
c.rfind('m')
12
c.index('t')
1
c.rindex('t')
14
c.index('z')
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    c.index('z')
ValueError: substring not found
c.count('i')
3
c.count('g')
1
c.count('t')
2
c.count('k')
0
c.replace('String', 'Float')
'Float is immutable'
c.replace('i','o')
'Strong os ommutable'
c.maketrans('aeiou','12345')
{97: 49, 101: 50, 105: 51, 111: 52, 117: 53}
c.translate(c.maketrans('aeiou','12345'))
'Str3ng 3s 3mm5t1bl2'
c.translate(c.maketrans('aeiou','*****'))
'Str*ng *s *mm*t*bl*'
c.split()
['String', 'is', 'immutable']
'String,is,immutable'.split()
['String,is,immutable']
'String,is,immutable'.split(',')
['String', 'is', 'immutable']
'String is immutable'.rsplit()
['String', 'is', 'immutable']
'String is immutable'.rsplit('-')
['String is immutable']
s='''
python
programming
lang'''
s
'\npython\nprogramming\nlang'
s.splitlines()
['', 'python', 'programming', 'lang']
''.join(['python', 'programming', 'lang'])
'pythonprogramminglang'
>>> '-'.join(['python', 'programming', 'lang'])
'python-programming-lang'
>>> ' '.join(['python', 'programming', 'lang'])
'python programming lang'
>>> ', '.join(['python', 'programming', 'lang'])
'python, programming, lang'
>>> ','.join([1,2,3])
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    ','.join([1,2,3])
TypeError: sequence item 0: expected str instance, int found
>>> 'python.py'.partition('.')
('python', '.', 'py')
>>> s.partition(',')
('\npython\nprogramming\nlang', '', '')
>>> s='java,python,c++')
SyntaxError: unmatched ')'
>>> s='java,python,c++'
>>> s.partition(',')
('java', ',', 'python,c++')
>>> s.rpartition(',')
('java,python', ',', 'c++')
>>> c= '        Hello         World      '
>>> c
'        Hello         World      '
>>> c.strip()
'Hello         World'
>>> c.lstrip()
'Hello         World      '
>>> c.rstrip()
'        Hello         World'
>>> #strip deal with spaces
>>> 
>>> text = "Hello 🙂"
>>> text.encode()
b'Hello \xf0\x9f\x99\x82'
>>> b'Hello \xf0\x9f\x99\x82'.decode()
'Hello 🙂'
>>> 
>>> 
