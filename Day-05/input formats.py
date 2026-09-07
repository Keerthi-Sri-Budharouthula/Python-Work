Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
x=input()
fyudgfgwfgwufgwu
x
'fyudgfgwfgwufgwu'
name=input()
keerthi
name
'keerthi'
name=input("Enter your name:")
Enter your name:keerthi
name
'keerthi'
age= input("Enter the age:")
Enter the age:21
age
'21'
type(age)
<class 'str'>
int(age)
21
age= int(input())
21
type(age)
<class 'int'>
price=float(input("enter the price:"))
enter the price:99
price
99.0
names=("enter the name:").split()
names= input("enter the names:").split()
enter the names:1 2 3 4 5 6
names
['1', '2', '3', '4', '5', '6']
map (int, names)
<map object at 0x000001A26297FF00>
list(map(int,names))
[1, 2, 3, 4, 5, 6]
values=list(map(int,input().split()))
1 2 3 45 6 7 7 6556754
values
[1, 2, 3, 45, 6, 7, 7, 6556754]
values=list(map(float,input().split()))
1 2 3454 5463.23
values
[1.0, 2.0, 3454.0, 5463.23]
names=tuple(input("Enter the names:").split())
Enter the names:423.554 43.787 898.32
names
('423.554', '43.787', '898.32')
values= tuple(map(float,input().split()))
567 5678 567
values
(567.0, 5678.0, 567.0)
names=set(input().split())
uiuyu hguu hiiu
names
{'hguu', 'hiiu', 'uiuyu'}
values =set(map(int,input().split()))
1 2 3 4
values
{1, 2, 3, 4}
values=set(map(float,input().split()))
1 2 3 4 
values
{1.0, 2.0, 3.0, 4.0}
a,b=[1,2]
a
1
b
2
a,b=(1,2)
a
1
b
2
email,password=input("Enter the email and password:").split()
Enter the email and password:keerthi@gmail.com 12345
email
'keerthi@gmail.com'
password
'12345'
int(password)
12345
a,b,c=list(map(int,input().split()))
1 2 3
a
1
b
2
c
3
name,marks=input().split()
keerthi 83
name
'keerthi'
int(marks)
83
e=eval(input())
1
e
1
e=eval(input())
1234.13
e
1234.13
>>> e=eval(input))
SyntaxError: unmatched ')'
>>> e=eval(input())
"keerthi"
>>> e
'keerthi'
>>> e=eval(input())
[1,2,3,4,4,6]
>>> e
[1, 2, 3, 4, 4, 6]
>>> e=eval(input())
[1,12.3,"str",[1,2,3]]
>>> e
[1, 12.3, 'str', [1, 2, 3]]
>>> e=eval(input())
(1,2,3,4)
>>> e
(1, 2, 3, 4)
>>> e=eval(input())
[1,2,3,4,6]
>>> e
[1, 2, 3, 4, 6]
>>> e=eval(input())
{1,2,3,4,5}
>>> e
{1, 2, 3, 4, 5}
>>> e=eval(input())
{1:1,2:2,3:3}
>>> e
{1: 1, 2: 2, 3: 3}
>>> e=eval(input())
True
>>> e
True
>>> e=eval(input())
2+3*4+5*8
>>> e
54
