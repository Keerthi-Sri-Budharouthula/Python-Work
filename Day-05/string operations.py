Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> s=''
>>> s
''
>>> s='codegnan'
>>> s
'codegnan'
>>> #string operations
>>> #concatination
>>> 'codegnan' + 'PFS'
'codegnanPFS'
>>> 'codegnan'*10 #repeatation
'codegnancodegnancodegnancodegnancodegnancodegnancodegnancodegnancodegnancodegnan'
>>> '_*_'*20
'_*__*__*__*__*__*__*__*__*__*__*__*__*__*__*__*__*__*__*__*_'
>>> 
>>> s='codegnan'#indexing
>>> s[4]
'g'
>>> s[-1]
'n'
>>> s[1]
'o'
>>> s[-2]
'a'
>>> names ='sajid abdul keerthi '
>>> names[0]
's'
>>> names[6]
'a'
>>> namess[-1]
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    namess[-1]
NameError: name 'namess' is not defined. Did you mean: 'names'?
>>> names[-1]
' '
>>> names[-2]
'i'
>>> #slicing
>>> #s[start:end+1:step]=>s[0:len:1]
names[0:5]
'sajid'
names[:5]
'sajid'
names
'sajid abdul keerthi '
names[6:11]
'abdul'
names[12:18]
'keerth'
names[12:19]
'keerthi'
names[12:]
'keerthi '
names[-1:-8]
''
names[-1:-8:-1]
' ihtree'
names[-1:-9:-1]
' ihtreek'
names[::-1]
' ihtreek ludba dijas'
names[:5:2]
'sjd'
'sajid' in names
True
'karthik' not in names
True
'keerthi' not in names
False
'keerthi' in names
True
