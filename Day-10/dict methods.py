Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
d={'name':'sajid','batch':63,'course':'PFS'}
data['name']
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    data['name']
NameError: name 'data' is not defined
data={'name':'sajid','batch':63,'course':'PFS'}
data['name']
'sajid'
data['batch']
63
data['course']
'PFS'
63 in data
False
data['age']
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    data['age']
KeyError: 'age'
data.get('age','key is not present')
'key is not present'
data.get('course','key is not present')
'PFS'
data['batch']=64
data
{'name': 'sajid', 'batch': 64, 'course': 'PFS'}
data['skills']=['python','mysql','flask']
data
{'name': 'sajid', 'batch': 64, 'course': 'PFS', 'skills': ['python', 'mysql', 'flask']}
data['age']=21
data
{'name': 'sajid', 'batch': 64, 'course': 'PFS', 'skills': ['python', 'mysql', 'flask'], 'age': 21}
data.update({'phno':9876783664,'email':'sajid@gmail.com'})
data
{'name': 'sajid', 'batch': 64, 'course': 'PFS', 'skills': ['python', 'mysql', 'flask'], 'age': 21, 'phno': 9876783664, 'email': 'sajid@gmail.com'}
data.pop('age')
21
data
{'name': 'sajid', 'batch': 64, 'course': 'PFS', 'skills': ['python', 'mysql', 'flask'], 'phno': 9876783664, 'email': 'sajid@gmail.com'}
data.pop('phno')
9876783664
data
{'name': 'sajid', 'batch': 64, 'course': 'PFS', 'skills': ['python', 'mysql', 'flask'], 'email': 'sajid@gmail.com'}
del data['name']
data
{'batch': 64, 'course': 'PFS', 'skills': ['python', 'mysql', 'flask'], 'email': 'sajid@gmail.com'}
data.popitem()
('email', 'sajid@gmail.com')
data
{'batch': 64, 'course': 'PFS', 'skills': ['python', 'mysql', 'flask']}
data.popitem()
('skills', ['python', 'mysql', 'flask'])
data
{'batch': 64, 'course': 'PFS'}
data.clear()
data
{}
data.keys()
dict_keys([])
data={'name': 'sajid', 'batch': 64, 'course': 'PFS', 'skills': ['python', 'mysql', 'flask'], 'age': 21, 'phno': 9876783664, 'email': 'sajid@gmail.com'}
data.keys()
dict_keys(['name', 'batch', 'course', 'skills', 'age', 'phno', 'email'])
data.values()
dict_values(['sajid', 64, 'PFS', ['python', 'mysql', 'flask'], 21, 9876783664, 'sajid@gmail.com'])
data.items()
dict_items([('name', 'sajid'), ('batch', 64), ('course', 'PFS'), ('skills', ['python', 'mysql', 'flask']), ('age', 21), ('phno', 9876783664), ('email', 'sajid@gmail.com')])
sorted(data)
['age', 'batch', 'course', 'email', 'name', 'phno', 'skills']
sorted(data,reverse=True)
['skills', 'phno', 'name', 'email', 'course', 'batch', 'age']
max(data)
'skills'
min(data)
'age'
data
{'name': 'sajid', 'batch': 64, 'course': 'PFS', 'skills': ['python', 'mysql', 'flask'], 'age': 21, 'phno': 9876783664, 'email': 'sajid@gmail.com'}
data.pop('age')
21
data['age']
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    data['age']
KeyError: 'age'
>>> data.get('age')
>>> data.setdefault('age',0)
0
>>> data.setdefault('name','')
'sajid'
>>> data
{'name': 'sajid', 'batch': 64, 'course': 'PFS', 'skills': ['python', 'mysql', 'flask'], 'phno': 9876783664, 'email': 'sajid@gmail.com', 'age': 0}
>>> len(data)
7
>>> all(data)
True
>>> any(data)
True
>>> a={1:1,2:2}
>>> b=a
>>> b[3]=3
>>> a
{1: 1, 2: 2, 3: 3}
>>> b
{1: 1, 2: 2, 3: 3}
>>> c=a.copy()
>>> c[4]=2
>>> c
{1: 1, 2: 2, 3: 3, 4: 2}
>>> aa
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    aa
NameError: name 'aa' is not defined. Did you mean: 'a'?
>>> a
{1: 1, 2: 2, 3: 3}
>>> d=dict.fromkeys(["a","b"],0)
>>> d
{'a': 0, 'b': 0}
